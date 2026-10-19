%global source0_hash d9de6d8fb7072228463bf61843159419c969edb34b3cef51832b516ae7972765
%global gem_name nenv
%global with_tests 1
Name:           rubygem-%{gem_name}
Version:        0.3.0
Release:        19%{?dist}
Summary:        Convenience wrapper for Ruby's ENV
License:        MIT
URL:            https://github.com/e2/nenv
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{name}-%{version}-specs.tgz
BuildArch:      noarch
%if 0%{?with_tests}
%endif
# oreon:deps
BuildRequires:  rubygem(coveralls)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Using ENV is like using raw SQL statements in your code. We all know how that
ends...

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n %{gem_name}-%{version} -a1

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

%if 0%{?with_tests}
cp -pr spec/ .%{gem_instdir}
pushd .%{gem_instdir}
rspec -r spec_helper
rm -rf spec
popd
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-nenv-doc -f %{oreon_filedir}/rubygem-nenv-doc.list

%changelog

%autochangelog
