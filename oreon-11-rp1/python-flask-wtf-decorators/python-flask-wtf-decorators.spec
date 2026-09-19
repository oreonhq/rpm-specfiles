%global source0_hash d7948797c39e4955ede531b2f6b89a42d0edfbd9273d6d5c6de811f6d7a42e20

%global srcname flask-wtf-decorators
%global commit 7fa5a26946d2fdb5b00d07251c0ca7d0e358fc1d
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           python-%{srcname}
Version:        0.1.2
Release:        0.23.20200715.%{shortcommit}%{?dist}
Summary:        Use decorators to validate forms
BuildArch:      noarch

License:        MIT
URL:            https://github.com/simpleapples/flask-wtf-decorators
Source0:        https://github.com/simpleapples/flask-wtf-decorators/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

%package -n python3-%{srcname}
Summary:       %{summary}
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-flask-wtf

%global _description %{expand:
Flask-WTF-Decorators is easy to use. You can define a view that requires
validation.

    from flask-wtf-decorators import FormValidator

    form_validator = FormValidator()

    @form_validator.validate_form(TestForm)
    @app.route('/', methods=['GET', 'POST'])
    def index(form):
        pass

You can tell Flask-WTF-Decorators what to do when a form is illegal.
To do this you should provide a callback for error_handler.

    @form_validator.error_handler
    def error_handler(errors):
        return jsonify(\{'errors': errors\}), 400
}

%description %_description
%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{commit}

%check
%python3 -m unittest discover -v -s tests

%build
%py3_build

%install
%py3_install

%files -n python3-%{srcname}
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/flask_wtf_decorators
%{python3_sitelib}/Flask_WTF_Decorators-*.egg-info/

%changelog
%autochangelog
