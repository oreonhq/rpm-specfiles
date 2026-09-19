%global source0_hash a9260f397f42e36de62764a8fe7e68bdbbcc75674d0419e831f633d6dda44936

%global gem_name comp_tree

Name:           rubygem-%{gem_name}
Version:        1.1.3
Release:        26%{?dist}
Summary:        A simple framework for automatic parallelism

License:        MIT
URL:            http://quix.github.io/comp_tree/
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# https://github.com/quix/comp_tree/pull/1
Patch1:         0001-Make-it-work-with-Minitest-5.patch
Patch2:         0002-Make-tests-work-with-Rake-10.patch
Patch3:         0003-Fix-throw_test-test.patch
Patch4:         0004-Fix-run-with-Minitest-5.patch
Patch5:         0005-minitest6.patch
BuildArch:      noarch

BuildRequires:  rubygems-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)
Requires:       ruby(release) >= 1.8
Requires:       rubygems
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
CompTree is a parallel computation tree structure based upon concepts from
pure functional programming.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
gem spec %{SOURCE0} -l --ruby >%{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
rake test

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_instdir}/devel
%exclude %{gem_cache}
%exclude %{gem_instdir}/*.rdoc
%exclude %{gem_instdir}/test
%exclude %{gem_instdir}/Rakefile
%{gem_spec}
%doc *.rdoc

%files doc
%{gem_docdir}

%changelog
%autochangelog
