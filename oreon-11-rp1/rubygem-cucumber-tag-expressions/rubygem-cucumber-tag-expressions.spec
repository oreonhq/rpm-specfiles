%global source0_hash 157d26663b7e0cf450f9b16a4d9835527c82b5008633fd9eb62927b06f9a7e33
%global gem_name cucumber-tag-expressions
Name: rubygem-%{gem_name}
Version: 4.0.2
Release:        11%{?dist}
Summary:        Cucumber tag expressions for ruby
License: MIT
URL: https://cucumber.io/docs/cucumber/api/#tag-expressions
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
Provides: rubygem-cucumber-tag_expressions = %{version}-%{release}
Obsoletes: rubygem-cucumber-tag_expressions < 2.0.2-10
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Cucumber tag expressions for ruby.

%package doc
Summary: Documentation for %{name}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-cucumber-tag-expressions-doc -f %{oreon_filedir}/rubygem-cucumber-tag-expressions-doc.list

%changelog

%autochangelog
