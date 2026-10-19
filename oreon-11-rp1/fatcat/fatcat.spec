%global source0_hash 5574f715f62a9feda7fffc8099f8bca7134ff4f1274bb1bc0db96a2969eea206
%bcond_without tests
Name:           fatcat
Version:        1.1.1
Release:        1%{?dist}
Summary:        FAT filesystems explore, extract, repair, and forensic tool
License:        MIT
URL:            https://github.com/Gregwar/fatcat
Source0:        https://github.com/Gregwar/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/pull/43.patch
ExcludeArch:    %{ix86}
%if %{with tests}
%endif
Suggests:       %{name}-doc
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  phpunit10
BuildRequires:  sed
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with tests}
%check

PATH="%{buildroot}/%{_bindir}:${PATH}" phpunit10
%endif
%files -f %{oreon_filedir}/main.list
%files -n fatcat-doc -f %{oreon_filedir}/fatcat-doc.list

%changelog

%autochangelog
