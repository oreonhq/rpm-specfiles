Summary: File system tree viewer
Name: tree-pkg
Version: 2.3.1
Release: 1%{?dist}

# The entire source code is LGPL-2.1-or-later except strverscmp.c
# which is LGPL-2.1-or-later.
License: GPL-2.0-or-later AND LGPL-2.1-or-later

URL: https://oldmanprogrammer.net/source.php?dir=projects/tree
Source: https://github.com/Old-Man-Programmer/tree/archive/refs/tags/%{version}.tar.gz

BuildRequires: gcc
BuildRequires: git-core
BuildRequires: make

# prevent rpmlint from reporting incorrect-fsf-address
# Sent upstream via email 20210920
Patch1: tree-license-fsf-addr.patch

# Keep file size field length constant regardless of whether SI units
# are used (bug #997937).
# Sent upstream via email 20210920
Patch2: tree-size-field-len.patch

# fix programming mistakes detected by static analysis
# Sent upstream via email 20181106
Patch3: tree-static-analysis.patch

# fix programming mistakes detected by static analysis
# Upstream is not active
Patch4: tree-static-analysis-2.patch
# oreon url source checksums begin
%global source0_sha256 621ff2b4faf214d7023143f6f9d496117c7c75131927837750b904140aff48a1
%global source0_file 2.3.1.tar.gz
# oreon url source checksums end

%description
The source RPM package of tree, which has to be named differently due to
limitations of Pagure and Gitlab.

%package -n tree
Summary: File system tree viewer

%description -n tree
The tree utility recursively displays the contents of directories in a
tree-like format.  Tree is basically a UNIX port of the DOS tree
utility.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/2.3.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "621ff2b4faf214d7023143f6f9d496117c7c75131927837750b904140aff48a1" || { echo "oreon: Source0 SHA256 mismatch for 2.3.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n tree-%{version} -S git

# do not escape UTF-8 chars in file names by default in UTF-8 locale (#1480778)
sed -e 's/LINUX/__linux__/' -i tree.c

%build
%make_build CFLAGS="$CFLAGS $(getconf LFS_CFLAGS)" LDFLAGS="$LDFLAGS"

%install
%make_install DESTDIR=$RPM_BUILD_ROOT%{_bindir} \
	      MANDIR=$RPM_BUILD_ROOT%{_mandir}

%files -n tree
%{_bindir}/tree
%{_mandir}/man1/tree.1*
%license LICENSE
%doc README

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.3.1-1
- Prepare for Oreon 11 (RP1)
