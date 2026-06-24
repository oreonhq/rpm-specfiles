%global source0_hash none

Summary:        A simple, lightweight interface to Amazon Web Services
Name:           python-boto
Version:        2.49.0
Release:        31%{?dist}
License:        MIT
URL:            https://github.com/boto/boto
Source0:        https://pypi.io/packages/source/b/boto/boto-%{version}.tar.gz
# Taken from sourcecode 2014-07-31
Source1:        boto-mit-license.txt

# Unbundle python-six
# https://github.com/boto/boto/pull/3086
Patch1:         boto-2.39.0-devendor.patch

# Add NAT gateway support
# https://github.com/boto/boto/pull/3472
Patch2:         boto-2.40.0-nat-gateway.patch

# Fix max_retry_delay config option
# https://github.com/boto/boto/pull/3506
# https://github.com/boto/boto/pull/3508
Patch4:         boto-2.40.0-retry-float.patch

# Add aws-exec-read to S3's canned ACL list
# https://github.com/boto/boto/pull/3332
Patch5:         boto-2.40.0-aws-exec-read.patch

# Add new instance attributes
# https://github.com/boto/boto/pull/3077
# https://github.com/boto/boto/pull/3131
Patch6:         boto-2.40.0-instance-attributes.patch

# Fix multi-VPC hosted zone parsing
# https://github.com/boto/boto/pull/2882
Patch7:         boto-2.40.0-multi-vpc-zone.patch

# Fix request logging for S3 requests
# https://github.com/boto/boto/issues/2722
# https://github.com/boto/boto/pull/2875
Patch8:         boto-2.40.0-s3-requestlog.patch

# Allow route53 health check resource paths to be none
# https://github.com/boto/boto/pull/2866
Patch9:         boto-2.40.0-route53-no-resourcepath.patch

# Add ModifySubnetAttribute support
# https://github.com/boto/boto/pull/3111
Patch10:        boto-2.45.0-modifysubnetattribute.patch

# tests: remove direct usages of mock in favor compat module
# https://fedoraproject.org/wiki/Changes/RemovePythonMockUsage
# https://github.com/boto/boto/pull/3952
Patch11:        remove-python-mock.patch

BuildRequires:  python3-devel
BuildRequires:  python3-six
# boto/plugin.py and boto/pyami/launch_ami.py uses imp
BuildRequires:  (python3-zombie-imp if python3 >= 3.12)
# test requires, but tests are commented out
# BuildRequires:  python3-httpretty
# BuildRequires:  python3-mock
# BuildRequires:  python3-nose
# BuildRequires:  python3-requests

BuildArch:      noarch


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


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel

%install
%pyproject_install
rm -f $RPM_BUILD_ROOT/%{_bindir}/*


%check
#%{__python3} tests/test.py default
%py3_check_import boto


%files -n python3-boto
%license boto-mit-license.txt
%{python3_sitelib}/boto*


%changelog
%autochangelog

