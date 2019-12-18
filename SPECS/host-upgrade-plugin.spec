Name: host-upgrade-plugin
Version: 2.2.0
Release: 1
Summary: Host upgrade plugin
License: GPL

Source0: https://code.citrite.net/rest/archive/latest/projects/XS/repos/host-upgrade-plugin/archive?at=v2.2.0&format=tar.gz&prefix=host-upgrade-plugin-2.2.0#/host-upgrade-plugin-2.2.0.tar.gz


Provides: gitsha(https://code.citrite.net/rest/archive/latest/projects/XS/repos/host-upgrade-plugin/archive?at=v2.2.0&format=tar.gz&prefix=host-upgrade-plugin-2.2.0#/host-upgrade-plugin-2.2.0.tar.gz) = 74c128154b3fd6c1e0b7ee18718e0af62899056f

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
