%global source0_hash 0f9e320ee62e668160f3de7c2dcfaac7a7cd57e77dc6909645a8e615444cd209
%global gem_name parse-cron
Name: rubygem-%{gem_name}
Version: 0.1.4
Release:        1%{?dist}
Summary:        Parses cron expressions and calculates the next occurrence
License: MIT
URL: https://github.com/siebertm/parse-cron
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(release)
Requires: ruby(rubygems) 
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
parses cron expressions and calculates the next occurrence 
after a given date

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

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
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec/
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-parse-cron-doc -f %{oreon_filedir}/rubygem-parse-cron-doc.list

%changelog

%autochangelog
