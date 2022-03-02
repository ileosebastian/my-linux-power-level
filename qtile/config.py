
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# My imports
import os
import subprocess
from libqtile import hook
import arcobattery
import widcpu



mod = "mod4"
terminal = guess_terminal()

##### My variables
# Dracula Color Palette
background = "#282a36"
current_line = "#44475a"
foreground = "#f8f8f2"
comment = "#6272a4"
cyan = "#8be9fd"
green = "#50fa7b"
orange = "#ffb86c"
pink = "#ff79c6"
purple = "#bd93f9"
red = "#ff5555"
yellow = "#f1fa8c"


default_font = "Agave Nerd Font"
default_font_size = 16

bar_bg_color = background
bar_size = 28


#### My functions
def get_separator():
    return widget.Sep( # separator
                    linewidth = 5,
                    padding = 0,
                    foreground=current_line,
                    background=background,
                    size_percent=100
                )



'''
    KEYS
'''
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # My key bindings
    # >>> Spawn programs
    Key([mod], "m", lazy.spawn("rofi -show drun"), desc="Open Rofi Menu"), 
    Key([mod], "f", lazy.spawn("firefox"), desc="Open Firefox"), 
    Key([mod], "s", lazy.spawn("spotify"), desc="Open Spotify"),
    # Key([mod, "mod1"], "l", lazy.spawn("i3lock -c 282a36"), desc="Lockscreen enable"),
    # Key(["control", "mod1"], "l", lazy.spawn("dm-tool lock"), desc="Lockscreen enable"),
    Key(["control", "mod1"], "l", lazy.spawn("i3lock -i /home/ileosebastian/Pictures/Wallpapers/berserker_into_white.png"), desc="Lockscreen enable"),
    Key(["control", "mod1"], "o", lazy.spawn("oblogout"), desc="Lockscreen enable"),
    Key([mod], "e", lazy.spawn("thunar"), desc="Open Files Manager"),
    Key([mod], "p", lazy.spawn("flameshot gui"), desc="Take a screenshot"),


    # >>> Set Volumen
    Key(
        [], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -q sset 'Master' 5%+")
    ),
    Key(
        [], "XF86AudioLowerVolume",
        lazy.spawn("amixer -q sset 'Master' 5%-")
    ),
    Key(
        [], "XF86AudioMute",
        lazy.spawn("amixer -q sset 'Master' toggle")
    ), 

    # >>> Set Brightness
    Key(
        [], "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl -s set +5%")
    ),
    Key(
        [], "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl -s set 5%-")
    ),
]

'''
    GROUPS
'''
groups = [
    Group(i) for i in [
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
    ] 
]

for i, group in enumerate(groups):
    n_group = str(i+1)
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], n_group, lazy.group[group.name].toscreen(),
            desc="Switch to group {}".format(group.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], n_group, lazy.window.togroup(group.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

groups.append(Group(""))
keys.extend([
    Key([mod], "0", lazy.group[groups[9].name].toscreen(),
            desc="Switch to group {}".format(group.name)),

    Key([mod, "shift"], "0", lazy.window.togroup(groups[9].name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(group.name)),
])

# Set keybinding to navigate much better
keys.extend([
    Key([mod, "control"],"Left", lazy.screen.prev_group()),
    Key([mod, "control"], "Right", lazy.screen.next_group()),
    Key(["control", "mod1"],"Tab", lazy.screen.prev_group()),
    Key(["mod1"], "Tab", lazy.screen.next_group()),
])


'''
    LAYOUTS
'''
layouts = [
    layout.Columns(
        border_focus=green,
        border_focus_stack=[comment, green],
        border_normal=current_line,
        border_width=3,
        margin=10
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    
    # layout.TreeTab(
    #     active_bg=green,
    #     active_fg=background,
    #     inactive_bg=current_line,
    #     inactive_fg=foreground,
    #     bg_color=background,
    #     font=default_font,
    #     sections=["Window Tabs", "Other tasks"],
    #     section_fg=foreground,
    #     section_fontsize=16,
    #     section_padding=12,
    #     vspace=10
    # ),

    # layout.VerticalTile(),
    # layout.Zoomy(),
]

'''
    WIDGETS
'''
widget_defaults = dict(
    font=default_font,
    # font='DaddyTimeMono',
    fontsize=default_font_size,
    padding=2,
)
extension_defaults = widget_defaults.copy()

# my_cpu = widcpu.NewMyLeoCPU(**widget_defaults)


'''
    SCREENS
'''
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    active=green,
                    this_current_screen_border=comment,
                    this_screen_border=yellow,
                    inactive=current_line,
                    urgent_alert_method='block',
                    urgent_border=red,
                    foreground=foreground,
                    disable_drag=True,
                    highlight_method='block',
                    border=red,
                    borderwidth=1,
                    font='sans',
                    fontsize=38,
                    padding=0,
                    padding_x=8, padding_y=1,
                    margin=10,
                    margin_x=0, margin_y=4
                ),
                widget.Spacer(),
                widget.Net(
                    background=pink,
                    foreground=foreground,
                    format="{down}   {up}",
                    interface="wlp1s0"
                ),
                get_separator(),
                widget.HDDBusyGraph(
                    background=background,
                    border_color=current_line,
                    fill_color=comment,
                    graph_color=cyan,
                    type="linefill",
                    space_type="used"
                ),
                get_separator(),
                widget.Memory(
                    background=orange,
                    foreground=background,
                    fmt="﬙{}",
                    measure_mem="M"
                ),
                get_separator(),
                widget.CPU(
                    background=yellow,
                    foreground=background,
                    fmt=" {}",
                    format="{freq_current}GHz {load_percent}%"
                ),
                # widcpu.CPU(**widget_defaults),
                # get_separator(),
                # widcpu.CPU(
                #     background=yellow,
                #     foreground=background,
                #     fmt=" {}",
                #     format="{freq_current}GHz {load_percent}%"
                # ),
                get_separator(),
                widget.ThermalSensor(
                    background=current_line,
                    tag_sensor="Tctl",
                    fmt="  {} | ",
                ),
                widget.ThermalSensor(
                    background=current_line,
                    tag_sensor="edge",
                    fmt=" {}",
                ),
                # widget.Mpris2(name='clementine', stop_pause_text=''),
                get_separator(),
                widget.Mpris2(
                    background=green,
                    foreground=comment,
                    name="spotify",
                    objname="org.mpris.MediaPlayer2.spotify",
                    display_metadata=['xesam:title', 'xesam:artist'],
                    scroll_chars=None,
                    stop_pause_text=''
                ),
                get_separator(),
                widget.TextBox(
                    background=red,
                    foreground=foreground,
                    font='sans',
                    fontsize=32,
                    fmt="",
                    padding=5,
                    mouse_callbacks={
                        "Button1": lazy.spawn("oblogout")
                    }
                ), 
            ],
            bar_size,
            background=bar_bg_color,
            border_width=[2, 2, 0, 2],  # Draw top and bottom borders
            border_color=["#44475a", "#44475a", current_line, "#44475a"]
        ),
        top=bar.Bar(
            [   
                widget.CurrentLayoutIcon(
                    background=background,
                    foreground=red,
                    scale=0.8,
                    fontsize=20,
                    padding=5,
                ),
                get_separator(),
                widget.WindowName(
                    foreground=foreground,
                    fontsize=16,
                    padding=5,
                    fmt=" {}"
                ),
                widget.Prompt(
                    background=current_line,
                    foreground=pink
                ),
                widget.Spacer(), 
                widget.Systray(
                    background=current_line,
                    icon_size=22,
                    padding=5
                ),
                get_separator(),
                widget.CheckUpdates(
                    background=yellow,
                    colour_have_updates=red,
                    colour_no_updates=background,
                    fontsize=20,
                    padding=5,
                    display_format="{updates} ﮮ",
                    no_update_string="0 ﮮ",
                    update_interval=3600,
                    distro="Arch_checkupdates"
                ),
                get_separator(),
                widget.Backlight(
                    background=foreground,
                    foreground=background,
                    backlight_name="amdgpu_bl0",
                    fmt="{} |"
                ),
                widget.Battery(
                    background=foreground,
                    low_background=red,
                    low_foreground=foreground,
                    foreground=background,
                    # format="{char} {percent:2.0%} {hour:d}:{min:02d} {watt:.2f} W",
                    format="{char} {percent:2.0%}",
                    charge_char="",
                    discharge_char="",
                    empty_char="",
                    full_char="F",
                    update_interval=10,
                ),
                arcobattery.BatteryIcon(
                    padding=-1,
                    scale=0.8,
                    y_poss=1,
                    scaleadd=1,
                    theme_path="/home/ileosebastian/.config/qtile/resources/battery_icons_horiz",
                    update_interval=5,
                    background=foreground
                ),
                get_separator(),
                widget.Clock(
                    # format='%Y-%m-%d %a %I:%M %p',
                    # format='%d/%m/%Y %A %H:%M',
                    format=' %d/%m/%Y %A  神 %H:%M',
                    font="Agave Nerd Font Bold",
                    background=purple,
                    foreground=background
                ),
                get_separator(),
                widget.Volume(
                    background=cyan,
                    foreground=current_line,
                    fmt="  {}"
                ),
            ],
            (bar_size-6),
            background=bar_bg_color,
            border_width=[0, 2, 2, 2],  # Draw top and bottom borders
            border_color=["#44475a", "#44475a", current_line, "#44475a"]  # Borders are magenta
        ),
    ),
]


'''
    MOUSE LAYOUTS
'''
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

'''
    VARIABLE SETTINGS
'''
dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry
        Match(wm_class="oblogout"),
        Match(wm_class="notification"),
    ],
    border_focus=current_line,
    border_normal=comment,
    border_width=1
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
# 
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


'''
    FUNCTIONS
'''
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    # widcpu.NewMyLeoCPU()
