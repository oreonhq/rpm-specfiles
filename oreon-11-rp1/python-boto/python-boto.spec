%global source0_hash ea0d3b40a2d852767be77ca343b58a9e3a4b00d9db440efb8da74b4e58025e5a
Summary:        A simple, lightweight interface to Amazon Web Services
Name:           python-boto
Version:        2.49.0
Release:        31%{?dist}
License:        MIT
URL:            https://github.com/boto/boto
Source0:        https://pypi.io/packages/source/b/boto/boto-%{version}.tar.gz
Source1:        boto-mit-license.txt
Patch1:         boto-2.39.0-devendor.patch
Patch2:         boto-2.40.0-nat-gateway.patch
Patch4:         boto-2.40.0-retry-float.patch
Patch5:         boto-2.40.0-aws-exec-read.patch
Patch6:         boto-2.40.0-instance-attributes.patch
Patch7:         boto-2.40.0-multi-vpc-zone.patch
Patch8:         boto-2.40.0-s3-requestlog.patch
Patch9:         boto-2.40.0-route53-no-resourcepath.patch
Patch10:        boto-2.45.0-modifysubnetattribute.patch
Patch11:        remove-python-mock.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-boto = %{version}-%{release}
# /oreon:deps
%description
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports over thirty services, such as S3 (Simple Storage Service),
SQS (Simple Queue Service), and EC2 (Elastic Compute Cloud) via their
REST and Query APIs.  The goal of boto is to support the full breadth
and depth of Amazon Web Services.  In addition, boto provides support
for other public services such as Google Storage in addition to private
cloud systems like Eucalyptus, OpenStack and Open Nebula.

%package -n python3-boto
Summary:        A simple, lightweight interface to Amazon Web Services
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-rsa
Requires:       (python3-zombie-imp if python3 >= 3.12)
%description -n python3-boto
Boto is a Python package that provides interfaces to Amazon Web Services.
It supports over thirty services, such as S3 (Simple Storage Service),
SQS (Simple Queue Service), and EC2 (Elastic Compute Cloud) via their
REST and Query APIs.  The goal of boto is to support the full breadth
and depth of Amazon Web Services.  In addition, boto provides support
for other public services such as Google Storage in addition to private
cloud systems like Eucalyptus, OpenStack and Open Nebula.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n boto-%{version}

#rm -r boto/vendored

cp -p %{SOURCE1} .

%build

%pyproject_wheel
%install
%pyproject_install
rm -f $RPM_BUILD_ROOT/%{_bindir}/*
%oreon_autofiles python3-boto usr/lib/python3*/site-packages/boto* usr/lib64/python3*/site-packages/boto* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/boto* usr/lib64/python3*/site-packages/boto* usr/bin/*

%check

%py3_check_import boto
%files
%files -n python3-boto -f %{oreon_filedir}/python3-boto.list

%changelog

%autochangelog

