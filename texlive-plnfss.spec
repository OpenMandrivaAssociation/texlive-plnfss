# revision 15878
# category Package
# catalog-ctan /macros/plain/plnfss
# catalog-date 2008-05-21 10:21:02 +0200
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-plnfss
Version:	1.1
Release:	1
Summary:	Font selection for Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/plnfss
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plnfss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/plnfss.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Plnfss is a set of macros to provide easy font access (somewhat
similar to NFSS but with some limitations) with Plain TeX.
Plnfss can automatically make use of PSNFSS fd files, i.e.,
when an Adobe Type 1 is used the relevant fd file will be
loaded automatically. For cmr-like fonts (ec, vnr, csr or plr
fonts), a special format called pfd (plain fd) is required and
must be loaded manually. See ot1cmr.pfd for further
information.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/plnfss/MIKmathf.tex
%{_texmfdistdir}/tex/plain/plnfss/ams.pfd
%{_texmfdistdir}/tex/plain/plnfss/il2cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/il2cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/ly1lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot1cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot1cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/ot4cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/plnfss.tex
%{_texmfdistdir}/tex/plain/plnfss/qxlm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t1lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5cm.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5cmr.pfd
%{_texmfdistdir}/tex/plain/plnfss/t5lm.pfd
%{_texmfdistdir}/tex/plain/plnfss/ts1lm.pfd
%doc %{_texmfdistdir}/doc/plain/plnfss/LPPL.txt
%doc %{_texmfdistdir}/doc/plain/plnfss/plnfss.txt
%doc %{_texmfdistdir}/doc/plain/plnfss/test-plnfss.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
