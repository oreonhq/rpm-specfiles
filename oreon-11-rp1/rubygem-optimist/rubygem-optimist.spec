%global source0_hash 336b753676d6117cad9301fac7e91dab4228f747d4e7179891ad3a163c64e2ed

%global gem_name optimist

%bcond check 0

Name:           rubygem-%{gem_name}
Version:        3.0.1
Release:        9%{?dist}
Summary:        Commandline option parser for Ruby

License:        MIT
URL:            https://rubygems.org/gems/optimist
Source:         https://rubygems.org/downloads/%{gem_name}-%{version}.gem
# https://github.com/ManageIQ/optimist/pull/140
Patch0:         optimist-pr140-minitest-5_20-compat.patch

BuildRequires:  rubygems-devel
%if %{with check}
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(chronic)
%endif

BuildArch:      noarch

%description
%{summary}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%if %{with check}

%check
# https://github.com/ManageIQ/optimist/issues/111
ruby -Ilib:test -e '$0="workaround"; Dir.glob "./test/**/*_test.rb", &method(:require)'

%endif

%files
%license %{gem_instdir}/LICENSE.txt
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/test/
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Rakefile
%exclude %{gem_instdir}/%{gem_name}.gemspec

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/FAQ.txt
%doc %{gem_instdir}/History.txt
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
