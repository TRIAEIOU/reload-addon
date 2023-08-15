import os
from aqt import mw, gui_hooks, QAction
from aqt.utils import chooseList
from .ankiutils import *

ADDON_PATH = os.path.dirname(__file__)
SEL_LBL = "Reload addon: select addon"
select_action: QAction
reload_action: QAction

VER = '1.0.0'

# Reload module ###################################################
def reload():
	"""Reload module"""
	import sys, importlib

	for module in [m for n, m in sys.modules.items() if n == CFG['Internal state']['Addon']]:
		try:
			importlib.reload(module)
		except:
			# there are some problems that are swept under the rug here
			pass

# Select addon ###########################################################
def select(*_):
	"""Select addon to reload (will store for future reloads)"""
	addons = mw.addonManager.allAddons()
	if (i := chooseList("Select addon", addons)) is not None:
		CFG['Internal state']['Addon'] = addons[i]
		mw.addonManager.writeConfig(__name__, CFG)
		update_label()

# Add menu items ########################################################
def init():
	global select_action, reload_action

	select_action = QAction(SEL_LBL)
	if sc := CFG.get('Select shortcut'):
		select_action.setShortcut(sc)
	select_action.triggered.connect(select)
	mw.form.menuTools.addAction(select_action)
	
	reload_action = QAction()
	if sc := CFG.get('Reload shortcut'):
		reload_action.setShortcut(sc)
	reload_action.triggered.connect(reload)
	mw.form.menuTools.addAction(reload_action)

	update_label()

def update_label():
	addon = CFG['Internal state'].get('Addon')
	lbl = f"Reload {addon if addon else '<none>'}"
	reload_action.setText(lbl)
	reload_action.setEnabled(addon in mw.addonManager.allAddons())

# Main ##################################################################
CFG = mw.addonManager.getConfig(__name__)
gui_hooks.main_window_did_init.append(init)

if strvercmp(VER, get_version()) > 0:
	set_version(VER)