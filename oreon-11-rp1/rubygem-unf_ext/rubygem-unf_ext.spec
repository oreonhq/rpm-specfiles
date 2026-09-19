%global source0_hash 926114a858934126c6bbfd3254347dadb5dae354711869368c0f75e3765fc6e9

%global	gem_name	unf_ext

Summary:	Unicode Normalization Form support library for CRuby
Name:		rubygem-%{gem_name}
Version:	0.0.9.1
Release:	9%{?dist}
# LICENSE.txt
# SPDX confirmed
License:	MIT
URL:		http://github.com/knu/ruby-unf_ext
Source0:	http://rubygems.org/gems/%{gem_name}-%{version}.gem

Requires:	ruby(release)
Requires:	ruby(rubygems)

BuildRequires:	ruby(release)
BuildRequires:	gcc-c++
BuildRequires:	rubygems-devel 
BuildRequires:	ruby-devel
# %%check
BuildRequires:	rubygem(test-unit)
Provides:	rubygem(%{gem_name}) = %{version}-%{release}

%description
Unicode Normalization Form support library for CRuby.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

pushd %{buildroot}
rm -f .%{gem_extdir_mri}/{gem_make.out,mkmf.log}
popd

# Remove the binary extension sources and build leftovers.
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.github/ \
	.gitignore \
	Gemfile \
	Rakefile \
	ext/ \
	test/ \
	*.gemspec \
	%{nil}
popd

%check
pushd .%{gem_instdir}
sed -i.orig \
	-e '/begin/,/end/d' \
	-e '/bundler/d' \
	test/helper.rb

sed -i -e '2i gem "test-unit"' test/helper.rb

ruby \
	-Ilib:test:.:%{buildroot}%{gem_extdir_mri} \
	test/test_unf_ext.rb

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md

%dir	%{gem_libdir}
%{gem_libdir}/%{gem_name}.rb
%{gem_libdir}/%{gem_name}/

%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
