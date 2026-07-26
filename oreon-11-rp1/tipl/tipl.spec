%global source0_hash 85af540294089b0ae2122442f9b119b4c711564857e89f4162b3b3fcbc3df935

%undefine __cmake_in_source_build
%global commit 6a5938047287eb90b63f441f3e5dd67fb5581408
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           tipl
Version:        0
Release:        0.22.git%{shortcommit}%{?dist}
Summary:        Template image processing library

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/frankyeh/TIPL
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/frankyeh/TIPL/pull/4
Patch0001:      0001-add-CMake-build-definitions-and-pkgconfig-file.patch
Patch0002:      0002-unbundle-SVM.patch

BuildRequires:  cmake
BuildRequires:  make
BuildArch:      noarch

%description
%{summary}.

%package        devel
Summary:        %{summary}
Requires:       libsvm-devel

%description    devel
Header-only template image processing library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n TIPL-%{commit} -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files devel
%license COPYRIGHT
%doc README.md
%{_includedir}/image.hpp
%{_includedir}/image/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
