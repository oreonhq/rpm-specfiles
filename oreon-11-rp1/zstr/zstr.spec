%global source0_hash b77ef8b961233a100a34da588962a95a2f3b00c9b2dc0ea67100b36ec72128af

# There are no ELF objects in this package, so turn off debuginfo generation.
%global debug_package %{nil}

Name:           zstr
Version:        1.1.0
Release:        %autorelease
Summary:        A C++ header-only ZLib wrapper

License:        MIT
URL:            https://github.com/mateidavid/zstr
VCS :           git:%{url}.git
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Use zlib-ng directly rather than via the compatibility interface
Patch:          %{name}-zlib-ng.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(zlib-ng)

# See https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global _desc %{expand:This C++ header-only library enables the use of C++ standard iostreams to
access ZLib-compressed streams.

For input access (decompression), the compression format is auto-detected, and
multiple concatenated compressed streams are decompressed seamlessly.

For output access (compression), the only parameter exposed by this API is the
compression level.}

%description
%_desc

%package devel
Summary:        A C++ header-only ZLib wrapper
BuildArch:      noarch
Requires:       pkgconfig(zlib-ng)
Provides:       %{name}-static = %{version}-%{release}

%description devel
%_desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
#%%cmake_install does nothing, so install manually
mkdir -p %{buildroot}%{_includedir}/zstr
install -m 0644 -p src/*.hpp %{buildroot}%{_includedir}/zstr

%check
%ctest

%files devel
%doc README.org
%license LICENSE
%{_includedir}/zstr/

%changelog
%autochangelog
