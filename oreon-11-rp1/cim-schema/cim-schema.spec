%global source0_hash c62993354a67425f8340d79285e7b335c220d010135f237b3ebc4f6485a8a922
%global source1_hash db2728548be18f0d17be645f7b2e3ee83bdf2b6f213a1d2e1337d206a95431f1
%global major 2
%global minor 55
%global update 0
Name:           cim-schema
Url:            http://www.dmtf.org/
Summary:        Common Information Model (CIM) Schema
Version:        %{major}.%{minor}.%{update}
Release:        4%{?dist}
License:        LicenseRef-DMTF
Source0:        https://www.dmtf.org/sites/default/files/cim/cim_schema_v2550/cim_schema_2.55.0Experimental-MOFs.zip
Source1:        https://www.dmtf.org/sites/default/files/cim/cim_schema_v2550/cim_schema_2.55.0Experimental-Doc.zip
Source2:        LICENSE
BuildArch:      noarch
# oreon:deps

# /oreon:deps
%package docs
Summary:        Common Information Model (CIM) Schema documentation
%description
Common Information Model (CIM) is a model for describing overall
management information in a network or enterprise environment. CIM
consists of a specification and a schema. The specification defines the
details for integration with other management models. The schema
provides the actual model descriptions.

Authors:
--------
    DTMF <http://www.dmtf.org/about/contact>

%description docs
Common Information Model (CIM) schema documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -T -a 1 -c -n %{name}-docs
%setup -q -T -a 0 -c -n %{name}-%{version}

%build

%install
MOFDIR=%{_datadir}/mof
CIMDIR=$MOFDIR/cimv%{version}
%__rm -rf $RPM_BUILD_ROOT
for i in `find . -name "*.mof"`; do
  sed -i -e 's/\r//g' $i
done
install -d $RPM_BUILD_ROOT/$CIMDIR
chmod -R go-wx .
chmod -R a+rX .
%__mv * $RPM_BUILD_ROOT/$CIMDIR/
ln -s cimv%{version} $RPM_BUILD_ROOT/$MOFDIR/cim-current
ln -s cim_schema_%{version}.mof $RPM_BUILD_ROOT/$MOFDIR/cim-current/CIM_Schema.mof
install -d $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/%{_docdir}/%{name}
cp -a %{SOURCE2} $RPM_BUILD_ROOT/%{_docdir}/%{name}
%oreon_autofiles cim-schema-docs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cim-schema-docs -f %{oreon_filedir}/cim-schema-docs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.55.0-4
- Import
