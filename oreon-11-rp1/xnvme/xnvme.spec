%global source0_hash d951a3115f686956f5c6b839b390ffb50bb443f7711fe35f57a07f4d0667277f

Name:           xnvme
Version:        0.7.5
Release:        6%{?dist}
Summary:        Unified API and tools for traditional and emerging I/O interfaces

License:        BSD-3-Clause
URL:            https://github.com/xnvme/xnvme
Source:         %{url}/releases/download/v%{version}/xnvme-%{version}.tar.gz

# Remove rpath from binaries
Patch1: 0001-remove-rpath.patch

# The package makes 64 bit assumptions so exclude 32 bit i686.
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  libaio-devel
BuildRequires:  liburing-devel

%description
%{summary}.
Minimal-overhead libraries and tools for cross-platform storage I/O and
NVMe-native development. A unified API encapsulating traditional block-I/O via
psync, libaio, and io_uring as well as user-space NVMe drivers.

%package devel
Summary:        Development library and header files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This contains the headers and libraries for developing against %{name}.

%package static
Summary:        Static library for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description static
%{summary}.

%package tools
Summary:        Command-line tools for storage I/O and NVMe-native development
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description tools
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson -Dforce_completions=true -Dwith-libvfn=disabled -Dwith-isal=disabled -Dwith-spdk=disabled -Dexamples=false -Dtests=false
%meson_build

%install
%meson_install

%check
%meson_test --num-processes 1

%files
%license LICENSE
%{_libdir}/lib%{name}.so.0*

%files devel
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/lib%{name}*.h

%files static
%{_libdir}/lib%{name}.a

%files tools
%{_bindir}/kvs
%{_bindir}/lblk
%{_bindir}/xdd
%{_bindir}/%{name}
%{_bindir}/%{name}-driver
%{_bindir}/%{name}_file
%{_bindir}/zoned
%{_mandir}/man1/kvs.1*
%{_mandir}/man1/kvs-*.1*
%{_mandir}/man1/lblk.1*
%{_mandir}/man1/lblk-*.1*
%{_mandir}/man1/xdd.1*
%{_mandir}/man1/xdd-*.1*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/%{name}-*.1*
%{_mandir}/man1/%{name}_file.1*
%{_mandir}/man1/%{name}_file-*.1*
%{_mandir}/man1/zoned.1*
%{_mandir}/man1/zoned-*.1*
%{bash_completions_dir}/kvs-completions
%{bash_completions_dir}/lblk-completions
%{bash_completions_dir}/xdd-completions
%{bash_completions_dir}/%{name}-completions
%{bash_completions_dir}/%{name}_file-completions
%{bash_completions_dir}/zoned-completions

%changelog
%autochangelog
