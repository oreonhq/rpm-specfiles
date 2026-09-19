%global source0_hash 5a0932f1fa82ce08a8516a2685d5a86031c000560f89946913c555a0697544be

%global gem_name http_parser.rb

Name:		rubygem-%{gem_name}
Version:	0.8.0
Release:	11%{?dist}
Summary:	Simple callback-based HTTP request/response parser
License:	MIT
URL:		https://github.com/tmm1/http_parser.rb
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/tmm1/http_parser.rb/pull/86
# Support ruby3_5 Ractor change
Patch0:	http_parser.rb-pr86-ruby35-Ractor-change.patch
BuildRequires:  gcc
BuildRequires:	rubygems-devel
BuildRequires:	ruby-devel
BuildRequires:	rubygem-rspec
%if 0%{?fedora} <= 20 || 0%{?el7}
Provides:	rubygem(%{gem_name}) = %{version}
%endif

%description
Ruby bindings to http://github.com/joylent/http-parser and
http://github.com/a2800276/http-parser.java.

%package doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{gem_name}-%{version} -p1

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

%if 0%{?fedora} || 0%{?rhel} >= 8
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -ar .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/
%else
mkdir -p %{buildroot}%{gem_extdir_mri}/lib
cp -ar .%{gem_instdir}/lib/ruby_http_parser.so %{buildroot}%{gem_extdir_mri}/lib
%endif

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/{ext/,.github/}

rm -f %{buildroot}%{gem_instdir}/{.gitignore,.gitmodules,Gemfile.lock}

# Run the test suite
%check
pushd .%{gem_instdir}
rspec -Ilib -I%{buildroot}%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{gem_libdir}
%{gem_extdir_mri}
%{gem_extdir_mri}/gem.build_complete
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/README.md
%license %{gem_instdir}/LICENSE-MIT
%doc %{gem_instdir}/Gemfile

%files doc
%doc %{gem_docdir}
%{gem_instdir}/%{gem_name}.gemspec
%{gem_instdir}/Rakefile
%{gem_instdir}/spec
%{gem_instdir}/bench
%{gem_instdir}/tasks

%changelog
%autochangelog
