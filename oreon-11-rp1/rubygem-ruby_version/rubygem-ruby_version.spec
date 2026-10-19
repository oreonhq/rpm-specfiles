%global source0_hash 5930f9950746b7e6c973184398ee364ee7440b170fef7922b9f5cdf317f1ccb5
%global gem_name ruby_version
Name:           rubygem-%{gem_name}
Version:        1.0.3
Release:        7%{?dist}
Summary:        Adds the RubyVersion pseudo-constant
License:        MIT
URL:            https://github.com/janlelis/ruby_version
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Provides a RubyVersion class which offers a convenient DSL for checking for
the right Ruby version.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec -Ilib
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ruby_version-doc -f %{oreon_filedir}/rubygem-ruby_version-doc.list

%changelog

%autochangelog
