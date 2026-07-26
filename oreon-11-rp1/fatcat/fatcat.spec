%global source0_hash 5574f715f62a9feda7fffc8099f8bca7134ff4f1274bb1bc0db96a2969eea206

%bcond_without tests

Name:           fatcat
Version:        1.1.1
Release:        %autorelease
Summary:        FAT filesystems explore, extract, repair, and forensic tool

License:        MIT
URL:            https://github.com/Gregwar/fatcat
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Port the test suite to PHPUnit 9+
Patch:          %{url}/pull/43.patch

# php-scl needed by phpunit10 not available
# and this package never gets released for ix86
ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  sed
%if %{with tests}
BuildRequires:  phpunit10
%endif

Suggests:       %{name}-doc

%description
fatcat is a tool is designed to manipulate FAT filesystems, in order to
explore, extract, repair, recover and forensic them. It currently supports
FAT12, FAT16 and FAT32.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description    doc
This package contains additional documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove bundled Windows-only dependency
rm -r src/xgetopt
sed -i '/xgetopt/d' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/fatcat.1

%if %{with tests}
%check
PATH="%{buildroot}/%{_bindir}:${PATH}" phpunit10
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/fatcat
%{_mandir}/man1/fatcat.1*

%files doc
%license LICENSE
%doc docs/*

%changelog
%autochangelog
