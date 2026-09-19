%global source0_hash b251552f6156f26db78fe542179ecfc7b8af0372ef0c9852eb30cdd1dcf54103

Name:           remake
Version:        0.16
Release:        %autorelease
Summary:        Build system that bridges the gap between make and redo

License:        GPL-3.0-or-later
URL:            https://github.com/silene/remake
VCS:            git:%{url}.git
Source:         %{url}/archive/%{name}-%{version}.tar.gz
# Find out which test is hanging
Patch:          %{name}-test.patch

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  doxygen-latex
BuildRequires:  gcc-c++
BuildRequires:  ghostscript
BuildRequires:  inotify-tools
BuildRequires:  tex-epstopdf
BuildRequires:  urw-base35-fonts

%description
Remake is a build system with features of both make and redo.  See the
documentation for details on usage and control file syntax.

%package doc
# The content is GPL-3.0-or-later.  Other licenses are due to files installed by
# doxygen.
# html/bc_s*.png: GPL-1.0-or-later
# html/clipboard.js: MIT
# html/closed.png: GPL-1.0-or-later
# html/cookie.js: MIT
# html/doc*.svg: GPL-1.0-or-later
# html/doxygen.css: GPL-1.0-or-later
# html/doxygen.svg: GPL-1.0-or-later
# html/dynsections.js: MIT
# html/folderclosed*.svg: GPL-1.0-or-later
# html/folderopen*.svg: GPL-1.0-or-later
# html/jquery.js: MIT
# html/menu.js: MIT
# html/menudata.js: MIT
# html/minus*.svg: GPL-1.0-or-later
# html/nav_*.png: GPL-1.0-or-later
# html/navtree.css: GPL-1.0-or-later
# html/open.png: GPL-1.0-or-later
# html/plus*.svg: GPL-1.0-or-later
# html/resize.js: MIT
# html/splitbar*.png: GPL-1.0-or-later
# html/sync_off.png: GPL-1.0-or-later
# html/sync_on.png: GPL-1.0-or-later
# html/tab_*.png: GPL-1.0-or-later
# html/tabs.css: GPL-1.0-or-later
License:        GPL-3.0-or-later AND GPL-1.0-or-later AND MIT
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
Provides:       bundled(js-jquery) = 3.6.0

%description doc
Documentation for using and developing %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0 -n %{name}-%{name}-%{version}

%build
g++ %{build_cxxflags} -D_GNU_SOURCE -o remake remake.cpp %{build_ldflags}
doxygen

%install
# Install the binary
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 remake %{buildroot}%{_bindir}

# Install the doxygen documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a doxydoc/html %{buildroot}%{_docdir}/%{name}

%check
cd testsuite
# Starting with Fedora 41, test t009 takes 10-12 hours to complete on s390x.
# Until we figure out the cause, skip that test.
%ifarch s390x
rm t009.sh
%endif
./all.sh

%files
%doc README.md
%exclude  %{_docdir}/%{name}/html
%{_bindir}/%{name}

%files doc
%doc %{_docdir}/%{name}
%exclude %{_docdir}/%{name}/README.md

%changelog
%autochangelog
