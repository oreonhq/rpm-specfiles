%global source0_hash 1ee7bc55c8dcec92cf7741a2132a9a6cd19e4b884fbc1b3aca23e1a4fcd92d55

# Generated from RedCloth-4.1.9.gem by gem2rpm -*- rpm-spec -*-
%global gem_name RedCloth

Name: rubygem-%{gem_name}
Version: 4.3.2
Release: 34%{?dist}
Summary: Textile parser for Ruby
License: MIT
URL: http://redcloth.org
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# Fixes failing tests on ARM which defaults to use unsigned char
# http://jgarber.lighthouseapp.com/projects/13054-redcloth/tickets/236-test-failure-on-armelpowerpc
Patch0: rubygem-redcloth-4.2.9-unsigned-char-fix.patch
# Fix Ruby 2.5 compatibility.
# https://github.com/jgarber/redcloth/pull/38/commits/00b55ace17ed408b1b6129e1ba6c90fd4f0a6d2c
Patch1: rubygem-RedCloth-4.3.2-Replace-deprecated-YAML-load_documents.patch
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: rubygem(rspec)
#BuildRequires: rubygem(rspec) < 3
#BuildRequires: rubygem(rspec-core) < 3
#BuildRequires: rubygem(rspec-mocks) < 3
#BuildRequires: rubygem(rspec-expectations) < 3
BuildRequires: ruby-devel
BuildRequires: gcc

%description
Textile parser for Ruby.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%patch 0 -p1
%patch 1 -p1

%build
gem build %{gem_name}.gemspec

%gem_install

# To create debuginfo file corretly (workaround for
# "#line" directive)
pushd .%{gem_instdir}/ext/redcloth_scan
mkdir ext
ln -sf .. ext/redcloth_scan
popd

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check 
pushd .%{gem_instdir}
rspec -I$(dirs +1)%{gem_extdir_mri} spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/redcloth
%{gem_extdir_mri}
%exclude %{gem_instdir}/.*
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%exclude %{gem_instdir}/redcloth.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.rdoc
%{gem_instdir}/Rakefile
%doc %{gem_instdir}/doc
%{gem_instdir}/spec
%{gem_instdir}/tasks

%changelog
%autochangelog
