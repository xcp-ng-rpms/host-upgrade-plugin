%global package_speccommit ee98c88d7afe62faad0689c93f4444d8f8c4c313
%global package_srccommit v3.0.1

Name: host-upgrade-plugin
Version: 3.0.1
Release: 1%{?xsrel}%{?dist}
Summary: Host upgrade plugin
License: GPL
Source0: host-upgrade-plugin-3.0.1.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
Requires: python3-xcp-libs >= 3.0.4-2
Requires: xapi-core
Requires: xen-dom0-tools

%description
Host upgrade plugin.

%prep
%autosetup -p1

%install
install -D -p prepare_host_upgrade.py %{buildroot}/etc/xapi.d/plugins/prepare_host_upgrade.py

%files
/etc/xapi.d/plugins/prepare_host_upgrade.py*


%changelog
* Fri Nov 08 2024 Frediano Ziglio <frediano.ziglio@cloud.com> - 3.0.1-1
- CA-392310: Handle LV mount point from URLs
- Allow specifying fs type in args for upgrade
- CP-51969: Add support for "platform" argument

* Thu Jun 06 2024 Frediano Ziglio <frediano.ziglio@cloud.com> - 3.0.0-2
- Add missing package dependencies

* Mon Feb 05 2024 Stephen Cheng <stephen.cheng@cloud.com> - 3.0.0-1
- CA-387145: Fix py2->py3 bugs
- CP-46691: Update python to python3

* Wed May 31 2023 Sola Zhang <sozhang@tibco.com> - 2.2.6-2
- CP-41922: Rebuild and bump the release number

* Fri May 26 2023 Sola Zhang <sozhang@tibco.com> - 2.2.6-1
- CP-41572: Add 'EULA' in file path for backward compatibility

* Tue Mar 21 2023 Sola Zhang <sozhang@tibco.com> - 2.2.5-1
- CP-41572: Fetch EUA through host-update-plugin

* Fri Aug 05 2022 Alex Brett <alex.brett@citrix.com> - 2.2.3-1
- CA-358877: Do not block upgrades to 8.2.1 because of partition layout

* Thu Apr 15 2021 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.2.2-1
- CP-35470: Prevent upgrades which need a legacy partition layout

* Tue Nov 05 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.2.0-1
- CA-329206: Get network settings from the correct PIF
- CP-31507: Add more detailed error codes
- Pylint cleanup

* Thu Oct 31 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.1.2-1
- CP-32358: Add HTTPS support
- CA-329412: Don't reveal if username doesn't have a password

* Thu Oct 24 2019 Ross Lagerwall <ross.lagerwall@citrix.com> - 2.1.1-1
- Remove code for outdated versions of Python
- CA-329412: Avoid logging HTTP/FTP passwords

* Wed Feb 06 2019 jenniferhe <jennifer.herbert@citrix.com> - 2.1.0-1
- CP-29836: Add an API to get the version from a URL
- CP-30501: Add a new API, getDom0DefaultMemory
- CP-29627: Make compatible with host-installer memory changes
- CP-23016 Provide errors with underscores

* Tue Jan 15 2019 rossla <ross.lagerwall@citrix.com> - 1.3.0-1
- CP-23016 Add more specific errors
- CP-30204: Fix running error
- CP-30204: Prevent upgrade from releases before 6.x in the RPU plugin

* Fri Oct 12 2018 Simon Rowe <simon.rowe@citrix.com> - 1.2.1-1
- CA-299552: add support for ramdisk-based upgrades

* Thu Aug 30 2018 Simon Rowe <simon.rowe@citrix.com> - 1.2.0-1
- CP-29028: add optional updates parameter to RPU plugin
- CP-29028: check host part of update URL matches main
- Add missing `return` on error path
- Add some documentation
- CP-21760: set one-shot boot entry

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
