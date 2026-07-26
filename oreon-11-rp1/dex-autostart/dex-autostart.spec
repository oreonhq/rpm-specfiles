%global source0_hash 661b96763b1cac062f872c78c03f150ed57d14e315720681bb1fb1e5362e29d4

Name:           dex-autostart
Version:        0.10.1
Release:        %autorelease
Summary:        Generate and execute DesktopEntry files

License:        GPL-3.0-or-later
URL:            https://github.com/jceb/dex
Source0:        https://github.com/jceb/dex/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-sphinx
BuildRequires: make
BuildArch:      noarch

%description
dex-autostart, DesktopEntry Execution, is a program to generate and execute
DesktopEntry files of the Application type.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n dex-%{version}

%build
%make_build VERSION=%{version}

# fix name in man page
sed -i "s/dex/dex-autostart/g" dex.1
sed -i "s/DEX/DEX-AUTOSTART/g" dex.1

# fix name in README
sed -i "s/dex/dex-autostart/g" README.rst
sed -i "s/DEX/DEX-AUTOSTART/g" README.rst

%install
%make_install PREFIX=/usr MANPREFIX=%{_mandir} NAME=%{name} VERSION=%{version}

# do not install the license twice
rm %{buildroot}/%{_defaultdocdir}/%{name}/LICENSE

%check
%{buildroot}/%{_bindir}/%{name} --test -v

%files
%license LICENSE
%{_defaultdocdir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%{_bindir}/%{name}

%changelog
%autochangelog
