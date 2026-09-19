%global source0_hash 51ab13ce8781c813c88a191eb7d5704ebde2a5d2417cf0e01fd46997748330a9

%global gem_name rdiscount

Name: rubygem-%{gem_name}
Version: 2.2.7.1
Release: 10%{?dist}
Summary: Fast Implementation of Gruber's Markdown in C
License: BSD-3-Clause
URL: http://dafoster.net/projects/rdiscount/
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby-devel
BuildRequires: libmarkdown-devel
BuildRequires: rubygem(test-unit)
BuildRequires: gcc

%description
RDiscount converts documents in Markdown syntax to HTML.

It uses the excellent Discount processor by David Loren Parsons for this
purpose, and thereby inherits Discount's numerous useful extensions to the
Markdown language.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

# Remove C and header files to unbundle discount-sources
find ext -type f \( -name "*.c" ! -name "rdiscount.c" -o -name "*.h" \) \
  -print -delete > discount_files

%gemspec_remove_file File.read("discount_files").lines(:chomp => true)

sed -i '/create_makefile/i $libs = "-lmarkdown"' ext/extconf.rb

%build
gem build ../%{gem_name}-%{version}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man7
mv %{buildroot}%{gem_instdir}/man/rdiscount.1 %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/man/markdown.7 %{buildroot}%{_mandir}/man7

# Copy C extensions to the extdir
mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

%check
pushd .%{gem_instdir}
ruby -I$(dirs +1)%{gem_extdir_mri} -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%dir %{gem_instdir}
%{_bindir}/rdiscount
%{gem_extdir_mri}
%license %{gem_instdir}/COPYING
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/*
# These used to be duplicated by discount package, but they are not anymore.
# Keeping these exluded while trying to figure out what is going on.
# https://bugzilla.redhat.com/show_bug.cgi?id=2140278
%exclude %{_mandir}/man7/markdown.7.gz

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/BUILDING
%doc %{gem_instdir}/README.markdown
%{gem_instdir}/Rakefile
%{gem_instdir}/man
%{gem_instdir}/rdiscount.gemspec
%{gem_instdir}/test

%changelog
%autochangelog
