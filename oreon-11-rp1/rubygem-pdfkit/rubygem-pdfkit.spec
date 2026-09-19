%global source0_hash cd99e9eef3fcfd3ba7932acdb31c05e41141904c025f1363e829c1b93503b7da

%global	gem_name	pdfkit

Name:		rubygem-%{gem_name}
Version:	0.8.7.3
Release:	7%{?dist}

Summary:	HTML+CSS to PDF using wkhtmltopdf
# SPDX confirmed
License:	MIT
 
URL:		https://github.com/pdfkit/pdfkit
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	git
BuildRequires:	rubygems-devel

BuildRequires:	wkhtmltopdf
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(mocha)
BuildRequires:	rubygem(simplecov)
BuildRequires:	rubygem(rack)
BuildRequires:	rubygem(rack-test)
BuildRequires:	rubygem(activesupport)
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	iputils
Requires:		wkhtmltopdf
BuildArch:		noarch

%description
Create PDFs using plain old HTML+CSS. Uses wkhtmltopdf
on the back-end which renders HTML using Webkit.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

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

# Clean up
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.github \
	.gitignore \
	.rspec \
	.ruby-gemset .ruby-version \
	.travis.yml \
	Gemfile Rakefile \
	POST_INSTALL \
	*.gemspec \
	spec/ \
	%{nil}
popd

%check
disable_test() {
	filename=$1
	shift
	num=$#
	while [ $num -gt 0 ]
	do
		sed -i -e "s|it \(\"$1\"\)|xit \1|" $filename
		shift
		num=$((num - 1))
	done
}

pushd .%{gem_instdir}

disable_test spec/configuration_spec.rb \
	"detects the existance of bundler" \
	%{nil}
ping -w3 www.google.co.jp || \
	disable_test spec/pdfkit_spec.rb \
	"can handle ampersands in URLs" \
	%{nil}

xvfb-run -n 98 rspec spec/
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc	%{gem_docdir}

%changelog
%autochangelog
