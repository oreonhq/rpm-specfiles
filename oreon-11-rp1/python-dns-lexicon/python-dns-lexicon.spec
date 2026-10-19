%global source0_hash a377bf2b4017ee46de8d5515cf2c204bfda74b49032dc5420bd3100993f28deb
Name:           python-dns-lexicon
Version:        3.25.2
Release:        1%{?dist}
Summary:        Manipulate DNS records on various DNS providers in a standardized/agnostic way
License:        MIT
URL:            https://dns-lexicon.github.io/dns-lexicon/introduction.html
Source0:        https://files.pythonhosted.org/packages/source/d/dns_lexicon/dns_lexicon-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-dns-lexicon-tox-config.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dns-lexicon = %{version}-%{release}
# /oreon:deps
%package -n       python3-dns-lexicon+route53
Summary:        Metapackage for python3-dns-lexicon route53 extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.28
Provides:       python3dist(dns-lexicon[route53]) = %{version}-%{release}

%description -n python3-dns-lexicon+route53
Metapackage for python3-dns-lexicon route53 extras.

%package -n       python3-dns-lexicon+localzone
Summary:        Metapackage for python3-dns-lexicon localzone extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(localzone) >= 0.9.8
Provides:       python3dist(dns-lexicon[localzone]) = %{version}-%{release}

%description -n python3-dns-lexicon+localzone
Metapackage for python3-dns-lexicon localzone extras.

%package -n       python3-dns-lexicon+softlayer
Summary:        Metapackage for python3-dns-lexicon softlayer extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(softlayer) >= 5
Provides:       python3dist(dns-lexicon[softlayer]) = %{version}-%{release}

%description -n python3-dns-lexicon+softlayer
Metapackage for python3-dns-lexicon softlayer extras.

%package -n       python3-dns-lexicon+gransy
Summary:        Metapackage for python3-dns-lexicon gransy extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(zeep) >= 3
Provides:       python3dist(dns-lexicon[gransy]) = %{version}-%{release}

%description -n python3-dns-lexicon+gransy
Metapackage for python3-dns-lexicon gransy extras.

%package -n       python3-dns-lexicon+oci
Summary:        Metapackage for python3-dns-lexicon oci extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(oci) >= 2
Provides:       python3dist(dns-lexicon[oci]) = %{version}-%{release}

%description -n python3-dns-lexicon+oci
Metapackage for python3-dns-lexicon oci extras.

%package -n       python3-dns-lexicon+qcloud
Summary:        Metapackage for python3-dns-lexicon qcloud extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(tencentcloud-sdk-python) >= 3
Provides:       python3dist(dns-lexicon[qcloud]) = %{version}-%{release}

%description -n python3-dns-lexicon+qcloud
Metapackage for python3-dns-lexicon qcloud extras.

%package -n       python3-dns-lexicon+full
Summary:        Metapackage for python3-dns-lexicon full extras
Requires:       python3-dns-lexicon = %{version}-%{release}
Requires:       python3dist(boto3) >= 1.28
Requires:       python3dist(localzone) >= 0.9.8
Requires:       python3dist(softlayer) >= 5
Requires:       python3dist(zeep) >= 3
Requires:       python3dist(oci) >= 2
Requires:       python3dist(tencentcloud-sdk-python) >= 3
Provides:       python3dist(dns-lexicon[full]) = %{version}-%{release}

%description -n python3-dns-lexicon+full
Metapackage for python3-dns-lexicon full extras.

%description

%package -n     python3-dns-lexicon
Summary:        Manipulate DNS records on various DNS providers in a standardized/agnostic way
# oreon:reqs
Requires:       python3dist(beautifulsoup4) >= 4
Requires:       python3dist(cryptography) >= 2
Requires:       python3dist(dnspython) >= 2
Requires:       python3dist(importlib-metadata) >= 4.6
Requires:       python3dist(pyotp) >= 2
Requires:       python3dist(pyyaml) >= 3
Requires:       python3dist(requests) >= 2
Requires:       python3dist(requests-unixsocket) >= 0.4
Requires:       python3dist(tldextract) >= 2
# /oreon:reqs
%description -n python3-dns-lexicon

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir dns_lexicon-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dns-lexicon usr/lib/python3*/site-packages/dns_lexicon* usr/lib64/python3*/site-packages/dns_lexicon* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dns_lexicon* usr/lib64/python3*/site-packages/dns_lexicon* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-dns-lexicon -f %{oreon_filedir}/python3-dns-lexicon.list

%changelog

%autochangelog
