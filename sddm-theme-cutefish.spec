%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name sddm-theme
%define git_refspec d3722b62c5b87b8bb88a7e2d75dbdefaadc7d1a2
%define git_refspec_short %(echo %{git_refspec} | cut -c -7)

Name: %{component_name}-cutefish
#Version: 0.0
Version: 0.0.0git.%(date +%Y%m%d).%{git_refspec_short}
Release: 1%{?dist}
License: GPLv3
Summary: SDDM Theme for Cutefish

Requires: sddm
Requires: libcutefish >= 0.2git.20210818.4caad74
Requires: fishui

Source0: https://github.com/cutefishos/%{component_name}/tarball/%{git_refspec}#/%{component_name}-%{git_refspec}.tar.gz

%description
SDDM Theme for Cutefish

%prep
%setup -qn cutefishos-%{component_name}-%{git_refspec_short}

%build

%install
mkdir -p %{buildroot}%{_datadir}/sddm/themes/cutefish/
cp -v *.qml %{buildroot}%{_datadir}/sddm/themes/cutefish/
cp -v system-shutdown-symbolic.svg %{buildroot}%{_datadir}/sddm/themes/cutefish/
cp -v theme.conf %{buildroot}%{_datadir}/sddm/themes/cutefish/

%files
%{_datadir}/sddm/themes/cutefish/FishUIMenu.qml
%{_datadir}/sddm/themes/cutefish/FishUIMenuItem.qml
%{_datadir}/sddm/themes/cutefish/Main.qml
%{_datadir}/sddm/themes/cutefish/SessionMenu.qml
%{_datadir}/sddm/themes/cutefish/UserView.qml
%{_datadir}/sddm/themes/cutefish/system-shutdown-symbolic.svg
%{_datadir}/sddm/themes/cutefish/theme.conf
