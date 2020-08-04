%global debug_package %{nil}

Name:           powerstat
Version:        0.02.24
Release:        1.0
Summary:        Laptop power measuring tool
License:        GPL-2.0
Group:          System/Monitoring
URL:            http://kernel.ubuntu.com/~cking/powerstat/
Source:         http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

%description
Powerstat measures the power consumption of a mobile PC that has a battery
power source. The output is like vmstat but also shows power consumption
statistics. At the end of a run, powerstat will calculate the average,
standard deviation and min/max of the gathered data. 

%prep
%setup -q

%build
#export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
%make_install

%files
%doc COPYING
%{_bindir}/powerstat
%{_mandir}/man8/powerstat.8*

%changelog
* Tue Aug 04 2020 Petr Sakar <petr.sakar@chare.eu> - 0.02.24
- update to version 0.02.24
  * Makefile: bump version
  * Debian/control: Add Rules-Requires-Root: no
- update to version 0.02.23
  * Makefile: bump minor version
  * Debian: remove compat, use debhelper-compat in Build-Depends
  * Makefile: respect standard prefix= variable (LP: #1877744)
  * zero the ws struct to clear static analysis warnings
- update to version 0.02.22
  * Makefile: bump version
  * Add bash command completion script
- update to version 0.02.21
  * Makefile: bump version
  * Ensure strlen on new_name is safe
  * file_get_uint64: ensure val is zero'd to fix static analysis warnings
  * Ensure power stats in p2 are initialized, fixes read if uninitialized values
  * Update copyright to 2020
- update to version 0.02.20
  * Makefile: bump version
  * Debian: update to compat level 12
  * Use snapcraft automatic versioning
- update to version 0.02.19
  * Makefile: bump version
  * Update copyright year
  * Make struct cpu_info pack more efficiently
- update to version 0.02.18
  * Makefile: bump version
  * Rename snapcraft directory to snap, add .travis.yml file to dist rule
  * Compute Geometric Mean without overflow with large sets of data
  * Add travis yaml file
- update to version 0.02.17
  * Makefile: bump version
  * voidify returns from log_printf call
  * Make indices arrays const
  * Make cpu_freq_scale const
  * Add hint on how to run if not in "discharge" mode
  * Add adjustable C-state column width for C-state name column
  * snapcraft: make confinement strict
  * snapcraft: add plugs
- update to version 0.02.16
  * Makefile: bump version
  * debian/copyright: use secure https url
  * debian/control: remove empty last line
  * update debian/compat to 11
  * Fix range of CPU frequencies histogram. Scale by 1000 and not 1e9
* Thu Feb 22 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.02.15
- Rebuild for Fedora
* Wed Jan 31 2018 mardnh@gmx.de
- update to version 0.02.15
  * Makefile: bump version
  * Fix spelling mistake in comment
  * Update copyright year
  * Add GNU format attribute to log_printf
* Wed Nov  1 2017 mardnh@gmx.de
- update to version 0.02.14
  * Makefile: bump version
  * Add geometic mean to statistics
* Fri Oct 20 2017 mardnh@gmx.de
- update to version 0.02.13
  * Makefile: bump version
  * Increase temp buf from 16 to 32 bytes, cleans up gcc warning
  * Add more scanf sanity checking
  * debian/control: update Standards-version to 4.1.1
  * voidify function returns
  * use sizeof an object rather than the objects type
  * Don't use sentinel for end of signals[], use array size instead
  * include <sys/uio.h> for writev
  * powerstat: break wide macro over 2 lines
* Wed Jun 21 2017 mardnh@gmx.de
- update to version 0.02.12
  * Makefile: bump version
  * Makefile: add snapcraft files to dist rule
  * Fix incorrect GPU stats when sample rate is not 1 second (LP: #1699134)
  * snapcraft: add default type and grade keys
  * snapcraft: Makefile: remove icon hack
  * reduce the scope of the variable 'buf'
  * snapcraft.yaml: remove bogos unnecessary libs
  * Add snapcraft files
  * update copyright year
* Wed May 10 2017 mardnh@gmx.de
- update to version 0.02.11
  * Makefile: bump version
  * Makefile: add mascot to dist rule
  * Remove two blank lines
  * Allow float compares a little slop
  * Makefile: add PEDANTIC flags
  * Add powerstat mascot
* Sat Jul 30 2016 mardnh@gmx.de
- update to version 0.02.10
  * Makefile: bump version
  * debian/control: update Standards-Version to 3.9.8
- update to version 0.02.09
  * Makefile: bump version
  * Do not overflow power domain and thermal zone buffers (LP: #1551297)
  * Tag RAPL stats as valid so stats show up in avg, std.dev. (LP: #1551287)
- update to version 0.02.08
  * Makefile: bump version
  * Move N/A message for GPU power right one char
  * Add some more per function comments
  * constify a few more func args
  * Make all non-main functions static
  * Minor fix up on GPU Watts field
  * Add GPU average stats
  * Clean up column formatting
  * add -g GPU stats
  * Update and correct copyright years
* Thu Feb 18 2016 mardnh@gmx.de
- update to version 0.02.07
  * Makefile: bump version
  * Manual: re-work some parts of the manual
  * Manual: add missong comma in SEE ALSO list
  * Move structure links to head of structures
  * Use a more efficient hashing function
* Wed Nov 11 2015 mardnh@gmx.de
- initial package
