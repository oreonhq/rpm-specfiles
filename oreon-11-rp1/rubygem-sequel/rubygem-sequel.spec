%global source0_hash cb0329b62287a01db68eead46759c14497a3fae01b174e2c41da108a9e9b4a12
%global gem_name sequel
Name: rubygem-%{gem_name}
Version: 5.100.0
Release:        1%{?dist}
Summary:        The Database Toolkit for Ruby
License: MIT
URL: http://sequel.jeremyevans.net
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: rubygem(bigdecimal)
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The Database Toolkit for Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sequel-doc -f %{oreon_filedir}/rubygem-sequel-doc.list

%changelog

%autochangelog
