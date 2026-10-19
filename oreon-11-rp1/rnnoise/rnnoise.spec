%global source1_hash 4ac81c5c0884ec4bd5907026aaae16209b7b76cd9d7f71af582094a2f98f4b43
%global source0_hash d12703c720e7bfd4ab2a96a95517bc7fb14806a0f4186e84bc3cfbaddce3d5dd
%global model_version 4ac81c5c0884ec4bd5907026aaae16209b7b76cd9d7f71af582094a2f98f4b43
Name:       rnnoise
Version:    0.2
%global forgeurl https://gitlab.xiph.org/xiph/rnnoise
%global tag v%{version}
%forgemeta
Release:        1%{?dist}
Summary:        Recurrent neural network for audio noise reduction
License:    BSD-3-Clause AND CC0-1.0
URL:        %{forgeurl}
Source0:        %{forgeurl}/-/archive/%{tag}/%{name}-%{tag}.tar.bz2
Source1:    https://media.xiph.org/rnnoise/models/rnnoise_data-%{model_version}.tar.gz
Patch0:     %{forgeurl}/-/commit/372f7b4b76cde4ca1ec4605353dd17898a99de38.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
RNNoise is a noise suppression library based on a recurrent neural network.

%package devel
Summary:    Devel files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}
%description devel
Devel files for %{name}.

%package doc
Summary:    Developer documentation for %{name}
Requires:   %{name} = %{version}-%{release}
BuildArch:  noarch
%description doc
The %{name}-doc package contains developer documentation for the %{name} package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1
tar -xf %{SOURCE1}

cat > 'package_version' <<-EOF
    PACKAGE_VERSION=%{version}
EOF

%build

autoreconf -fi
%configure \
%ifarch x86_64 %{ix86}
  --enable-x86-rtcd \
%endif
  --disable-static \
  %{nil}
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_pkgdocdir}/COPYING
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rnnoise-devel -f %{oreon_filedir}/rnnoise-devel.list
%files -n rnnoise-doc -f %{oreon_filedir}/rnnoise-doc.list

%changelog

%autochangelog
