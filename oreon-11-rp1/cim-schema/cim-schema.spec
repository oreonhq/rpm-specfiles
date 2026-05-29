%global source0_hash none
%global source1_hash none

#
# spec file for package cim-schema
#
# Copyright (c) 2009 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon.
#
# The license for this spec file is the MIT/X11 license:
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

# norootforbuild

%global major 2
%global minor 55
%global update 0

Name:           cim-schema
Url:            http://www.dmtf.org/
Summary:        Common Information Model (CIM) Schema
Version:        %{major}.%{minor}.%{update}
Release:        4%{?dist}
License:        LicenseRef-DMTF
Source0:        http://www.dmtf.org/standards/cim/cim_schema_v2550/cim_schema_Experimental-MOFs.zip
Source1:        http://www.dmtf.org/standards/cim/cim_schema_v2550/cim_schema_Experimental-Doc.zip
Source2:        LICENSE
BuildArch:      noarch

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
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%(test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; })
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

%files
%dir %{_datarootdir}/mof
%dir %{_datarootdir}/mof/cimv%{version}
%{_datarootdir}/mof/cimv%{version}/*
%{_datarootdir}/mof/cim-current
%doc %{_docdir}/%{name}/LICENSE

%files docs
%doc ../%{name}-docs/*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.55.0-4
- Import
