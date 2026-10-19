%global source1_hash dd3d447815881fcfad481eeab341d91c351bb21d2de835193664d9bbb1db9638
%global source0_hash b2080b350753a9ac4930869ded8e61a1d2151c01e03b0bf07b4675cbd9ce5372
%global gem_name net-ldap
Name: rubygem-%{gem_name}
Version: 0.20.0
Release:        1%{?dist}
Summary:        Net::LDAP for Ruby implements client access LDAP protocol
License: MIT
URL: http://github.com/ruby-ldap/ruby-net-ldap
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/ruby-ldap/ruby-net-ldap/archive/v%{version}/ruby-net-ldap-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(flexmock)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Net::LDAP for Ruby (also called net-ldap) implements client access for the
Lightweight Directory Access Protocol (LDAP), an IETF standard protocol for
accessing distributed directory services. Net::LDAP is written completely in
Ruby with no external dependencies. It supports most LDAP client features and
a subset of server features as well.
Net::LDAP has been tested against modern popular LDAP servers including
OpenLDAP and Active Directory. The current release is mostly compliant with
earlier versions of the IETF LDAP RFCs (2251–2256, 2829–2830, 3377, and
3771).
Our roadmap for Net::LDAP 1.0 is to gain full client compliance with
the most recent LDAP RFCs (4510–4519, plus portions of 4520–4532).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
tar zxf %{SOURCE1} ruby-net-ldap-%{version}/test --strip-components 1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

ruby -Itest -Ilib -e 'Dir.glob "./test/**/*.rb", &method(:require)'
%files -f %{oreon_filedir}/main.list
%files -n rubygem-net-ldap-doc -f %{oreon_filedir}/rubygem-net-ldap-doc.list

%changelog

%autochangelog
