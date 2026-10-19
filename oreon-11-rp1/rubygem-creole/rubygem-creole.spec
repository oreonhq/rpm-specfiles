%global source1_hash 1949e111fdf4261e1d584c8ce258eb25228166d8da49969885748e313bbe3348
%global source0_hash 951701e2d80760f156b1cb2a93471ca97c076289becc067a33b745133ed32c03
%global gem_name creole
Name: rubygem-%{gem_name}
Version: 0.5.0
Release:        1%{?dist}
Summary:        Lightweight markup language
License: Ruby OR BSD-2-Clause
URL: https://github.com/minad/creole
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://raw.githubusercontent.com/minad/creole/d0b49a67465ed70eacd4d88790f9462beb9ed068/LICENSE
Requires: ruby(release)
Requires: ruby(rubygems)
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(bacon)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Creole is a lightweight markup language (http://wikicreole.org/).

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

install -p -m 0644 %{SOURCE1} .

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
bacon -Ilib test/*_test.rb
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-creole-doc -f %{oreon_filedir}/rubygem-creole-doc.list

%changelog

%autochangelog
