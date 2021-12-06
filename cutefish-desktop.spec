%if %{fedora} == 34
%define fl_f34 1
%else
%define fl_f34 0
%endif

%if %{fedora} == 35
%define fl_f35 1
%else
%define fl_f35 0
%endif

Name: cutefish-desktop
Version: 0.20211206.1
Release: 0a%{?dist}
License: GPLv3
Summary: Cutefish Desktop

Requires: cutefish-desktop-common
Requires: falkon
Requires: calligra
Requires: sddm

# @core Packages
Requires: audit basesystem bash coreutils curl dhcp-client dnf e2fsprogs filesystem glibc grubby hostname iproute iputils kbd less man-db ncurses openssh-clients openssh-server parted passwd policycoreutils procps-ng rootfiles rpm selinux-policy-targeted setup shadow-utils sssd-common sssd-kcm sudo systemd util-linux vim-minimal yum NetworkManager dnf-plugins-core dracut-config-rescue fedora-repos-modular firewalld plymouth zram-generator-defaults
%if %{fl_f34}
Requires: systemd-oomd-defaults
%else
%endif

# @base-x Packages
Requires: glx-utils mesa-dri-drivers mesa-vulkan-drivers plymouth-system-theme xorg-x11-drv-amdgpu xorg-x11-drv-ati xorg-x11-drv-evdev xorg-x11-drv-fbdev xorg-x11-drv-intel xorg-x11-drv-libinput xorg-x11-drv-nouveau xorg-x11-drv-openchrome xorg-x11-drv-qxl xorg-x11-drv-vesa xorg-x11-drv-vmware xorg-x11-drv-wacom xorg-x11-server-Xorg xorg-x11-xauth xorg-x11-xinit
%ifarch armhf aarch64
Requires: xorg-x11-drv-armsoc
%endif

%if %{fl_f34}
Requires: xorg-x11-utils
%endif

# @input-method Packages
Requires: ibus-anthy ibus-cangjie-engine-cangjie ibus-hangul ibus-libpinyin ibus-libzhuyin ibus-m17n ibus-typing-booster im-chooser imsettings
Requires: ibus-qt imsettings-qt

# @dial-up Packages
Requires: ppp ModemManager NetworkManager-adsl NetworkManager-ppp NetworkManager-wwan lrzsz minicom

# @multimedia Packages
Requires: alsa-ucm alsa-utils gstreamer1-plugin-openh264 gstreamer1-plugins-bad-free gstreamer1-plugins-good gstreamer1-plugins-ugly-free 
%if %{fl_f34}
Requires: pipewire-alsa pipewire-gstreamer pipewire-pulseaudio pipewire-utils
%else
Requires: alsa-plugins-pulseaudio pulseaudio 
%endif
## extras
Recommends: gstreamer1-plugins-bad-freeworld gstreamer1-libav
Recommends: qt5-qtwebengine-freeworld

# @standard Packages
Requires: abrt-cli acl at attr bash-completion bc bind-utils btrfs-progs bzip2 cifs-utils compsize cpio crontabs cryptsetup cyrus-sasl-plain dbus default-editor deltarpm dos2unix dosfstools ed ethtool exfatprogs file fpaste fprintd-pam gnupg2 hunspell iptstate irqbalance jwhois logrotate lsof mailcap man-pages mcelog mdadm microcode_ctl mlocate mtr nano net-tools nfs-utils nmap-ncat ntfs-3g ntfsprogs opensc passwdqc pciutils pinfo psacct quota realmd rsync rsyslog smartmontools sos sssd sudo symlinks systemd-udev tar tcpdump time traceroute tree unzip usbutils util-linux-user wget which words zip
Requires: nano-default-editor

# @guest-desktop-agent Packages
Requires: hyperv-daemons open-vm-tools-desktop qemu-guest-agent spice-vdagent virtualbox-guest-additions

# @fonts Packages
Requires: aajohan-comfortaa-fonts abattis-cantarell-fonts dejavu-sans-fonts dejavu-sans-mono-fonts dejavu-serif-fonts google-noto-emoji-color-fonts google-noto-sans-cjk-ttc-fonts google-noto-sans-gurmukhi-fonts google-noto-sans-sinhala-vf-fonts jomolhari-fonts julietaula-montserrat-fonts khmer-os-system-fonts liberation-mono-fonts liberation-sans-fonts liberation-serif-fonts lohit-assamese-fonts lohit-bengali-fonts lohit-devanagari-fonts lohit-gujarati-fonts lohit-kannada-fonts lohit-odia-fonts lohit-tamil-fonts lohit-telugu-fonts paktype-naskh-basic-fonts pt-sans-fonts sil-abyssinica-fonts sil-mingzat-fonts sil-nuosu-fonts sil-padauk-fonts smc-meera-fonts stix-fonts thai-scalable-waree-fonts

Recommends: flatpak

# From cutefish-extras repository
Recommends: cutefish-desktop-common-extras

%description
This is the metapackage for Cutefish Desktop environment

%prep

%build

%install

%files
