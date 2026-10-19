%global source0_hash b090e317b98247fd701449e54fa5ed35e4f1cbfd934a8fe1bb12792ce9b80a32
%global gem_name idn
Name: rubygem-%{gem_name}
Version: 0.0.2
Release:        1%{?dist}
Summary:        Ruby Bindings for the GNU LibIDN library
License: Apache-2.0 AND LicenseRef-Callaway-LGPLv2+
URL: http://rubyforge.org/projects/idn/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-idn-0.0.2-Fix-for-ruby-1.9.x.patch
Patch1: rubygem-idn-0.0.2-ruby2-encoding-in-tests-fix.patch
Patch2: rubygem-idn-c99.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libidn-devel
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby Bindings for the GNU LibIDN library, an implementation of the Stringprep,
Punycode and IDNA specifications defined by the IETF Internationalized Domain
Names (IDN) working group. 

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch -P0 -p0
%patch -P1 -p1
%patch -P2 -p1

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
ruby -I$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/tc_*.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-idn-doc -f %{oreon_filedir}/rubygem-idn-doc.list

%changelog

%autochangelog
