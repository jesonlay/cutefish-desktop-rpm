Name: cutefish-extras-source
Version: 0.20210805
Release: 0a.extra
License: MIT
Summary: cutefish-extras-source repository

Requires: rpmfusion-free-release

%description
This package installs the cutefish-extras-source repository

%prep

%build

%install
mkdir -p %{buildroot}/%{_sysconfdir}/yum.repos.d
touch %{buildroot}/%{_sysconfdir}/yum.repos.d/rmnscnce_cutefish-extras-source.repo

%post
curl -s https://packagecloud.io/install/repositories/rmnscnce/cutefish-extras-source/script.rpm.sh | bash

%files
%ghost %{_sysconfdir}/yum.repos.d/rmnscnce_cutefish-extras-source.repo
