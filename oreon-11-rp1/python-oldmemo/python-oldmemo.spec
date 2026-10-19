%global source0_hash a925e921cc1cf0e203a8090b10898264cd89299087faf91893ef98b6140bc5ed
Name:           python-oldmemo
Version:        2.1.0
Release:        1%{?dist}
Summary:        Backend implementation of the namespace eu.siacs.conversations.axolotl
License:        AGPL-3.0-only
URL:            https://github.com/Syndace/python-oldmemo
Source0:        https://github.com/Syndace/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          relax-protobuf.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-oldmemo = %{version}-%{release}
# /oreon:deps
%package -n       python3-oldmemo+xml
Summary:        Metapackage for python3-oldmemo xml extras
Requires:       python3-oldmemo = %{version}-%{release}
Requires:       python3dist(xmlschema) >= 2.0.2
Provides:       python3dist(oldmemo[xml]) = %{version}-%{release}

%description -n python3-oldmemo+xml
Metapackage for python3-oldmemo xml extras.

%package -n       python3-oldmemo+docs
Summary:        Metapackage for python3-oldmemo docs extras
Requires:       python3-oldmemo = %{version}-%{release}
Provides:       python3dist(oldmemo[docs]) = %{version}-%{release}

%description -n python3-oldmemo+docs
Metapackage for python3-oldmemo docs extras.

%package -n       python3-oldmemo+lint
Summary:        Metapackage for python3-oldmemo lint extras
Requires:       python3-oldmemo = %{version}-%{release}
Provides:       python3dist(oldmemo[lint]) = %{version}-%{release}

%description -n python3-oldmemo+lint
Metapackage for python3-oldmemo lint extras.

%package -n       python3-oldmemo+dev
Summary:        Metapackage for python3-oldmemo dev extras
Requires:       python3-oldmemo = %{version}-%{release}
Provides:       python3dist(oldmemo[dev]) = %{version}-%{release}

%description -n python3-oldmemo+dev
Metapackage for python3-oldmemo dev extras.

%description

%package -n     python3-oldmemo
Summary:        Backend implementation of the namespace eu.siacs.conversations.axolotl
# oreon:reqs
Requires:       python3dist(cryptography) >= 3.3.2
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
%description -n python3-oldmemo

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
# Remove pre-generated files
rm oldmemo/oldmemo_pb2.py
rm oldmemo/oldmemo_pb2.pyi

%build

protoc --python_out=oldmemo/  oldmemo.proto
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook oldmemo.texi
popd # texinfo
popd # docs
%install
%pyproject_install
install -pDm0644 docs/texinfo/oldmemo.xml \
 %{buildroot}%{_datadir}/help/en/python-oldmemo/oldmemo.xml
%oreon_autofiles python3-oldmemo usr/lib/python3*/site-packages/oldmemo* usr/lib64/python3*/site-packages/oldmemo* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/oldmemo* usr/lib64/python3*/site-packages/oldmemo* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-oldmemo -f %{oreon_filedir}/python3-oldmemo.list

%changelog

%autochangelog
