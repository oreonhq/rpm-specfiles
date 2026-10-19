%global source0_hash 89c9d9ca8c1383e561271745f8229d8819d2cc6c708040ca5e7f459cef238b84
Name:           python-twomemo
Version:        2.1.0
Release:        1%{?dist}
Summary:        Implementation of the namespace `urn:xmpp:omemo:2` for python-omemo
License:        MIT
URL:            https://github.com/Syndace/python-twomemo
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          relax-protobuf-version.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-twomemo = %{version}-%{release}
# /oreon:deps
%package -n       python3-twomemo+xml
Summary:        Metapackage for python3-twomemo xml extras
Requires:       python3-twomemo = %{version}-%{release}
Requires:       python3dist(xmlschema) >= 2.0.2
Provides:       python3dist(twomemo[xml]) = %{version}-%{release}

%description -n python3-twomemo+xml
Metapackage for python3-twomemo xml extras.

%package -n       python3-twomemo+docs
Summary:        Metapackage for python3-twomemo docs extras
Requires:       python3-twomemo = %{version}-%{release}
Provides:       python3dist(twomemo[docs]) = %{version}-%{release}

%description -n python3-twomemo+docs
Metapackage for python3-twomemo docs extras.

%package -n       python3-twomemo+lint
Summary:        Metapackage for python3-twomemo lint extras
Requires:       python3-twomemo = %{version}-%{release}
Provides:       python3dist(twomemo[lint]) = %{version}-%{release}

%description -n python3-twomemo+lint
Metapackage for python3-twomemo lint extras.

%package -n       python3-twomemo+dev
Summary:        Metapackage for python3-twomemo dev extras
Requires:       python3-twomemo = %{version}-%{release}
Provides:       python3dist(twomemo[dev]) = %{version}-%{release}

%description -n python3-twomemo+dev
Metapackage for python3-twomemo dev extras.

%description

%package -n     python3-twomemo
Summary:        Implementation of the namespace `urn:xmpp:omemo:2` for python-omemo
# oreon:reqs
Requires:       python3dist(doubleratchet) < 2
Requires:       python3dist(doubleratchet) >= 1.2.0
Requires:       python3dist(omemo) < 3
Requires:       python3dist(omemo) >= 2.0.0
Requires:       python3dist(protobuf) >= 3.20.3
Requires:       python3dist(typing-extensions) >= 4.3.0
Requires:       python3dist(x3dh) < 2
Requires:       python3dist(x3dh) >= 1.2.0
Requires:       python3dist(xeddsa) < 2
Requires:       python3dist(xeddsa) >= 1.0.0
# /oreon:reqs
%description -n python3-twomemo

%package docs
Summary: Documentation for python-twomemo
BuildArch: noarch
%description docs

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove pre-generated files
rm twomemo/twomemo_pb2.py 
rm twomemo/twomemo_pb2.pyi 

%build

protoc --python_out=twomemo/  twomemo.proto
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook twomemo.texi
popd # texinfo
popd # docs
%install
%pyproject_install
install -pDm0644 docs/texinfo/twomemo.xml \
 %{buildroot}%{_datadir}/help/en/python-twomemo/twomemo.xml
%oreon_autofiles python3-twomemo usr/lib/python3*/site-packages/twomemo* usr/lib64/python3*/site-packages/twomemo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/twomemo* usr/lib64/python3*/site-packages/twomemo* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pyproject_check_import
%files
%files -n python3-twomemo -f %{oreon_filedir}/python3-twomemo.list
%files -n python-twomemo-docs -f %{oreon_filedir}/python-twomemo-docs.list

%changelog

%autochangelog
