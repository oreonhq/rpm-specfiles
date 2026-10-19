%global source0_hash none
%global forgeurl https://android.googlesource.com/platform/external/perfetto
%global common_description %{expand:
Perfetto is a production-grade open-source stack for performance
instrumentation and trace analysis. It offers services and libraries and for
recording system-level and app-level traces, native plus Java heap profiling, a
library for analyzing traces using SQL and a web-based UI to visualize and
explore multi-GB traces.}
Name:           perfetto
Version:        49.0
Release:        1%{?dist}
Summary:        System profiling, app tracing and trace analysis
License:        Apache-2.0
URL:            https://perfetto.dev/
Source0:        %{forgeurl}/+archive/v%{version}.tar.gz#/%{name}-v%{version}.tar.gz
Source1:        perfetto.tmpfiles
Source2:        perfetto.sysusers
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
ExclusiveArch:  aarch64 x86_64
# oreon:deps
BuildRequires:  binutils-gold
BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  gn
BuildRequires:  ninja-build
BuildRequires:  pandoc
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description    %{common_description}

%package        libs
Summary:        Libraries for %{name}
%description    libs %{common_description}

This package contains shared libraries for %{name}.

%package        sdk
Summary:        Perfetto Tracing SDK
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    sdk %{common_description}

This package contains the Perfetto Tracing SDK, a C++17 library that allows
userspace applications to emit trace events and add more app-specific context
to a Perfetto trace.

%prep
%oreon_prep
%build

gn gen build --args="\
  is_debug=false \
  use_custom_libcxx=false \
  is_hermetic_clang=false \
  is_system_compiler=true \
  is_clang=false \
  skip_buildtools_check=true \
  enable_perfetto_integration_tests=false \
  enable_perfetto_unittests=false \
  perfetto_use_system_protobuf=true \
  perfetto_use_system_zlib=true \
  perfetto_enable_git_rev_version_header=false \
  extra_cflags=\"${CFLAGS}\" \
  extra_cxxflags=\"${CXXFLAGS}\" \
  extra_ldflags=\"${LDFLAGS}\" \
  cc=\"${CC}\" \
  cxx=\"${CXX}\" \
  "
%ninja_build -C build perfetto traced traced_probes
pandoc docs/reference/perfetto-cli.md -s -t man --shift-heading-level-by=-1 \
  > perfetto.1
chrpath -d build/{perfetto,traced,traced_probes}
%install
install -Dpm0755 -t %{buildroot}%{_libdir} build/libperfetto.so
install -Dpm0755 -t %{buildroot}%{_sbindir} build/traced build/traced_probes
install -Dpm0755 -t %{buildroot}%{_bindir} build/perfetto
install -Dpm0644 -t %{buildroot}%{_unitdir} debian/{traced,traced-probes}.service
install -Dpm0664 -t %{buildroot}%{_mandir}/man1 perfetto.1
install -Ddpm0755 %{buildroot}/run/perfetto
install -Dpm0644 %SOURCE1 %{buildroot}%{_tmpfilesdir}/perfetto.conf
install -Dpm0644 %SOURCE2 %{buildroot}%{_sysusersdir}/perfetto.conf
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/configs test/configs/*.cfg
install -Dpm0644 -t %{buildroot}%{_datadir}/%{name}/sdk sdk/perfetto.{h,cc}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post traced.service traced-probes.service
%preun

%systemd_preun traced.service traced-probes.service
%postun

%systemd_postun_with_restart traced.service traced-probes.service
%files -f %{oreon_filedir}/main.list
%files -n perfetto-libs -f %{oreon_filedir}/perfetto-libs.list
%files -n perfetto-sdk -f %{oreon_filedir}/perfetto-sdk.list

%changelog

%autochangelog
