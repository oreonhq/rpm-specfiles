%global source0_hash 00d620939c710788ae3f71188ef913e0aa7ff0a5a39f48249213ea6215558c8d
%global gem_name jekyll-email-protect
Name: rubygem-%{gem_name}
Version: 1.1.0
Release:        1%{?dist}
Summary:        A simple liquid filter which converts emails into percent-encoded strings
License: MIT
URL: https://github.com/vwochnik/jekyll-email-protect
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/rspec
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(liquid)
BuildRequires:  rubygem(rspec-expectations)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Email protection liquid filter for Jekyll.

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
sed -i "/require 'jekyll'/ s/'jekyll'/'liquid'/" spec/spec_helper.rb
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-jekyll-email-protect-doc -f %{oreon_filedir}/rubygem-jekyll-email-protect-doc.list

%changelog

%autochangelog
