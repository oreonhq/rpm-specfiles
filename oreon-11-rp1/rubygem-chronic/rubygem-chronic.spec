%global source0_hash 766f2fcce6ac3cc152249ed0f2b827770d3e517e2e87c5fba7ed74f4889d2dc3

# Generated from chronic-0.2.3.gem by gem2rpm -*- rpm-spec -*-

%global gem_name chronic

Summary: A natural language date parser
Name: rubygem-%{gem_name}
Version: 0.10.2
Release: 26%{?dist}
License: MIT
URL: http://github.com/mojombo/chronic
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/mojombo/chronic/pull/414
Patch0:  chronic-pr414-minitest-5_19-compat.patch
# Fix compability with minitest 6
Patch1:  chronic-0.10.2-minitest6.patch

BuildRequires: ruby
BuildRequires: rubygems-devel
BuildRequires: rubygem(minitest) > 5
BuildArch: noarch

%description
Chronic is a natural language date/time parser written in pure Ruby.

%package doc
Summary: Documentation for %{name}
Requires:%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ruby -Itest -e 'Dir.glob "./test/**/test_*.rb", &method(:require)'
popd

%files
%exclude %{gem_instdir}/.*
%exclude %{gem_instdir}/%{gem_name}.gemspec
%dir %{gem_instdir}
%{gem_libdir}
%doc %{gem_instdir}/LICENSE
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/HISTORY.md
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/test

%changelog
%autochangelog
