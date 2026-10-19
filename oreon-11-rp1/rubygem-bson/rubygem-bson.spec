%global source0_hash c468c1e8a3cfa1e80531cc519a890f85586986721d8e305f83465cc36bb82608
%global gem_name bson
Name: rubygem-%{gem_name}
Version: 5.2.0
Release:        1%{?dist}
Summary:        Ruby implementation of the BSON specification
License: Apache-2.0
URL: http://bsonspec.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: rubygem(bigdecimal)
Requires: rubygem(json)
Provides: rubygem-bson_ext%{?_isa} = %{version}-%{release}
Provides: rubygem-bson_ext = %{version}-%{release}
Provides: rubygem(bson_ext) = %{version}-%{release}
Obsoletes: rubygem-bson_ext < 4.1.1-1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(base64)
BuildRequires:  rubygem(bigdecimal)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A fully featured BSON specification implementation in Ruby.

%package doc
Summary: Documentation for %{name}
License: Apache-2.0 AND MIT
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version}

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bson-doc -f %{oreon_filedir}/rubygem-bson-doc.list

%changelog

%autochangelog
