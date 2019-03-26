Name: host-upgrade-plugin
Version: 1.1.6
Release: 1%{dist}
Summary: Host upgrade plugin
License: GPL
Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/%{name}/archive?at=v%{version}&format=tar.gz&prefix=%{name}-%{version}#/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel

%description
Host upgrade plugin.

%prep
%autosetup -p1

%install
install -D -p prepare_host_upgrade.py %{buildroot}/etc/xapi.d/plugins/prepare_host_upgrade.py

%files
/etc/xapi.d/plugins/prepare_host_upgrade.py*


%changelog
* Wed May 30 2018 Simon Rowe <simon.rowe@citrix.com> - 1.1.6-1
- CA-290443: Use rt_answerfile when serial is in use

* Mon Apr 09 2018 Simon Rowe <simon.rowe@citrix.com> - 1.1.5-1
- CA-287020: Support RPUs when using iSCSI BFS

* Wed Mar 07 2018 Simon Rowe <simon.rowe@citrix.com> - 1.1.4-1
- CA-284060: Add VLAN support

* Tue Aug 08 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.1.3-1
- CA-261861: Fix safe2upgrade check on multipath root

* Mon Apr 10 2017 Ross Lagerwall <ross.lagerwall@citrix.com> - 1.1.2-2
- Build as noarch
- Require python2-devel as a build dependency

* Wed Mar 15 2017 Simon Rowe <simon.rowe@citrix.com> - 1.1.2-1
- CP-19638: Avoid repacking install image
