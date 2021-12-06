%define debug_package %{nil}
%define _build_id_links none
%define _disable_source_fetch 0

%define component_name screenlocker
#%%define git_refspec dc1f80daf8f6542bf5829d1f13209d79f90b6ae5
#%%define git_refspec_short %%(echo %%{git_refspec} | cut -c -7)

Name: cutefish-%{component_name}
Version: 0.5
#Version: %%{version}git.%%(date +%Y%m%d).%%{git_refspec_short}
Release: 1%{?dist}
License: GPLv3
Summary: System screen locker for Cutefish Desktop

BuildRequires: cmake
BuildRequires: libX11-devel
BuildRequires: qt5-qtbase-devel qt5-qtquickcontrols2-devel qt5-qttools-devel qt5-qtx11extras-devel qt5-linguist
BuildRequires: pam-devel

Provides: bundled(kcheckpass) = 5.22.4

Source0: https://github.com/cutefishos/%{component_name}/archive/refs/tags/%{version}.tar.gz
#Source0: https://github.com/cutefishos/%%{component_name}/tarball/%%{git_refspec}#/%%{component_name}-%%{git_refspec}.tar.gz

%description
System screen locker for Cutefish Desktop

%prep
%setup -qn %{component_name}-%{version}
#%%setup -qn cutefishos-%%{component_name}-%%{git_refspec_short}

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

%files
%{_bindir}/%{name}
%{_bindir}/ccheckpass
%{_datadir}/%{name}
