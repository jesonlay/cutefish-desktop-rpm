Name: cutefish-desktop-common
Version: 0.20210819.0
Release: 1%{?dist}
License: GPLv3
Summary: Common packages for Cutefish Desktop

BuildArch: noarch
Requires: libcutefish
Requires: cutefish-core
Requires: cutefish-qt-plugins cutefish-kwin-plugins
Requires: cutefish-icons sddm-theme-cutefish
Requires: cutefish-dock cutefish-launcher cutefish-statusbar
Requires: cutefish-screenlocker
Requires: cutefish-settings cutefish-calculator cutefish-filemanager cutefish-terminal

%description
This is the metapackage for Cutefish Desktop environment

%prep

%build

%install

%files
