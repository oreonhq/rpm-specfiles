%global source0_hash 2d0337188246bb00d878ab5d0e30f3a97a4ec34bfcf82d76e17cb75dc38cad37

Name:           act
%global lname   AutomaticComponentToolkit
%global goipath github.com/Autodesk/%{lname}
Version:        1.6.0
Release:        %autorelease
Summary:        Automatic Component Toolkit
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

%{?gometa}
%{?!gometa:BuildRequires: /usr/bin/go}

URL:            https://%{goipath}
Source0:        %{url}/archive/v%{version}/%{lname}-%{version}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if 0%{?fedora} >= 37 || 0%{?rhel} >= 10
ExcludeArch:    %{ix86}
%endif

%description
The Automatic Component Toolkit (ACT) is a code generator that takes an
instance of an Interface Description Language file and generates a thin
C89-API, implementation stubs and language bindings of your desired software
component.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{lname}-%{version}

%build
%{?!gobuild:%global gobuild go build -ldflags "-B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x}
%gobuild -o act Source/*.go

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 -vp act %{buildroot}%{_bindir}/

%files
%doc README.md
%license LICENSE.md
%{_bindir}/act

%changelog
%autochangelog
