%global source0_hash 951f35eaa17fa09e437802c84604c62eea1f84b512a335af85398e0f70ebfeaf
%global gem_name rspec-pending_for
Name:           rubygem-%{gem_name}
Version:        0.1.16
Release:        1%{?dist}
Summary:        Mark specs pending or skipped for specific Ruby engine
License:        MIT
URL:            https://github.com/pboling/rspec-pending_for
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{name}-%{version}-specs.tgz
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(ruby_engine)
BuildRequires:  rubygem(ruby_version)
BuildRequires:  rubygem(simplecov)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Mark specs pending or skipped for specific Ruby engine (e.g. MRI or JRuby) /
version combinations.

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
tar -xzf %{SOURCE1}

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

cp -a spec/ ./%{gem_instdir}
pushd .%{gem_instdir}
rspec -Ilib -rspec_helper spec
rm -rf spec/
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rspec-pending_for-doc -f %{oreon_filedir}/rubygem-rspec-pending_for-doc.list

%changelog

%autochangelog
