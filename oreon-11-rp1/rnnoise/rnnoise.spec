%global source0_hash d12703c720e7bfd4ab2a96a95517bc7fb14806a0f4186e84bc3cfbaddce3d5dd

# Update this value from //rnnoise/model_version. This is the sha256sum of the model tarball.
%global model_version 4ac81c5c0884ec4bd5907026aaae16209b7b76cd9d7f71af582094a2f98f4b43

Name:       rnnoise
Version:    0.2

%global forgeurl https://gitlab.xiph.org/xiph/rnnoise
%global tag v%{version}
%forgemeta

Release:    %autorelease
Summary:    Recurrent neural network for audio noise reduction

# The pretrained model is licensed under CC0.
# This is fine since:
#   - This work is not covered under any patents[^1].
#   - This is a machine learning model, which falls under the category of "content"[^2].
# ^1: https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/HB2GPMVKMTNP5WDGIRNU5NZUO4JWQPII/
# ^2: https://docs.fedoraproject.org/en-US/legal/license-approval/#_licenses_allowed_for_content
License:    BSD-3-Clause AND CC0-1.0

URL:        %{forgeurl}
Source0:    %forgesource
Source1:    https://media.xiph.org/rnnoise/models/rnnoise_data-%{model_version}.tar.gz

# Fix compiliation issues on aarch64.
Patch0:     %{forgeurl}/-/commit/372f7b4b76cde4ca1ec4605353dd17898a99de38.patch

BuildRequires: gcc

BuildRequires: libtool
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: make

BuildRequires: doxygen
BuildRequires: graphviz

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

%files
%license COPYING
%doc AUTHORS README
%{_libdir}/lib%{name}.so.0*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_pkgdocdir}/html/

%changelog
%autochangelog
