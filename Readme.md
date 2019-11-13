

# tl_switcher

Simple tool to run on active window on linux system.
I connect that with gnome shorcuts:

```
Super + i -> /home/tomek/workspace/my/tl_switcher/tlswitcher.py idea
Super + c -> /home/tomek/workspace/my/tl_switcher/tlswitcher.py google-chrome
Super + t -> /home/tomek/workspace/my/tl_switcher/tlswitcher.py terminator
```

## Tip

### Remap capslock to super

`setxkbmap -option caps:super`
`dconf write "/org/gnome/desktop/input-sources/xkb-options" "['caps:super']"`
