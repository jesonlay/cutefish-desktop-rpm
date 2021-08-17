%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name sddm-theme
%define git_refspec 994e1c68746876b370dfc17b96c10266f47c5a67
%define git_refspec_short %(echo %{git_refspec} | cut -c -7)

Name: %{component_name}-cutefish
#Version: 0.0
Version: 0.0.0git.%(date +%Y%m%d).%{git_refspec_short}
Release: 1%{?dist}
License: GPLv3
Summary: SDDM Theme for Cutefish

BuildRequires: cmake

Requires: sddm

Source0: https://github.com/cutefishos/%{component_name}/tarball/%{git_refspec}#/%{component_name}-%{git_refspec}.tar.gz

%description
SDDM Theme for Cutefish

%prep
%setup -qn cutefishos-%{component_name}-%{git_refspec_short}

%build
%{set_build_flags}
mkdir build
pushd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd
# clean up
rm -rv %{buildroot}/%{_sysconfdir}

%files
%{_datadir}/sddm/faces/.face.icon
%{_datadir}/sddm/themes/cutefish/FishUIMenu.qml
%{_datadir}/sddm/themes/cutefish/FishUIMenuItem.qml
%{_datadir}/sddm/themes/cutefish/Main.qml
%{_datadir}/sddm/themes/cutefish/SessionMenu.qml
%{_datadir}/sddm/themes/cutefish/UserView.qml
%{_datadir}/sddm/themes/cutefish/system-shutdown-symbolic.svg
%{_datadir}/sddm/themes/cutefish/theme.conf