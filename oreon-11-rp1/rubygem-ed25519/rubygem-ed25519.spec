%global source0_hash 514a5584f84d39daac568a17ec93a4e7261e140c52c562ed8c382c18456e627d
%global gem_name ed25519
Name: rubygem-%{gem_name}
Version: 1.3.0
Release:        1%{?dist}
Summary:        An efficient digital signature library providing the Ed25519 algorithm
License: MIT
URL: https://github.com/crypto-rb/ed25519
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-spec.txz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A Ruby binding to the Ed25519 elliptic curve public-key signature system
described in RFC 8032.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1

find -type f -iname '*.jar'

%gemspec_remove_file ["lib/ed25519_jruby.jar"]

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
ln -s %{_builddir}/spec .
sed -i -e '/^require .bundler\/setup./ s/^/#/g' \
  -e '/^require .coveralls./ s/^/#/g' \
  -e '/^Coveralls\./ s/^/#/g' \
  ./spec/spec_helper.rb
rspec -rspec_helper -I$(dirs +1)%{gem_extdir_mri} spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ed25519-doc -f %{oreon_filedir}/rubygem-ed25519-doc.list

%changelog

%autochangelog
