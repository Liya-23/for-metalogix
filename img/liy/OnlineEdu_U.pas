unit OnlineEdu_U;

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants,
  System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.ComCtrls,
  Vcl.Imaging.jpeg, Vcl.ExtCtrls, Vcl.Samples.Spin, MasterAccount_U, Vcl.Grids,
  Tables_U, clsNML_U;

type
  TfrmOnlineEdu = class(TForm)
    PageControl1: TPageControl;
    tbsWelcome: TTabSheet;
    tbsCourses: TTabSheet;
    btnAbout: TButton;
    btnCourses: TButton;
    btnExit: TButton;
    btnNext: TButton;
    Image1: TImage;
    lblFullName: TLabel;
    lblNML: TLabel;
    lblProgStu: TLabel;
    lblStudP: TLabel;
    tbsApplication: TTabSheet;
    tbsAPS: TTabSheet;
    imgKhazimla: TImage;
    imgKamva: TImage;
    imgMichelle: TImage;
    imgSiphosethu: TImage;
    imgAnathi: TImage;
    imgPhilela: TImage;
    imgLiyabona: TImage;
    imgOlwethu: TImage;
    imgNathan: TImage;
    imgAsisipho: TImage;
    lblLecture1: TLabel;
    lblCourse1: TLabel;
    lblLecture2: TLabel;
    lblCourse2: TLabel;
    lblLecture3: TLabel;
    lblCourse3: TLabel;
    lblLecture4: TLabel;
    lblCourse4: TLabel;
    lblLecture5: TLabel;
    lblCourse5: TLabel;
    lblLecture6: TLabel;
    lblCourse6: TLabel;
    lblLecture7: TLabel;
    lblCourse7: TLabel;
    lblLecture8: TLabel;
    lblCourse8: TLabel;
    lblLecture9: TLabel;
    lblCourse9: TLabel;
    lblLecture10: TLabel;
    lblCourse10: TLabel;
    btnAboutLect: TButton;
    Button1: TButton;
    btnAppply: TButton;
    btnExitt: TButton;
    cbxOptIII: TComboBox;
    btnWrite: TButton;
    rgpGender: TRadioGroup;
    cbxYear: TComboBox;
    edtHighSchool: TEdit;
    cbxOptII: TComboBox;
    cbxOptI: TComboBox;
    btnSubmit: TButton;
    cbxSource: TComboBox;
    edtApplyDate: TEdit;
    edtHomeAddress: TEdit;
    edtPostal: TEdit;
    edtHomeNo: TEdit;
    edtCellNo: TEdit;
    edtHL: TEdit;
    CheckBox1: TCheckBox;
    edtID: TEdit;
    edtName: TEdit;
    edtSurname: TEdit;
    lblSource: TLabel;
    lblDateComplete: TLabel;
    lblNameSchool: TLabel;
    lblPostal: TLabel;
    lblAddress: TLabel;
    lblHomeNum: TLabel;
    lblCellNum: TLabel;
    lblLanguageHL: TLabel;
    lblCitizen: TLabel;
    lblIDNum: TLabel;
    lblName: TLabel;
    lblSurname: TLabel;
    lblCourseOptI: TLabel;
    lblCourseOptIII: TLabel;
    lblCourseOptII: TLabel;
    lblAcademicYear: TLabel;
    Label2: TLabel;
    Label1: TLabel;
    sedEng: TSpinEdit;
    lblIT: TLabel;
    lblEnglish: TLabel;
    ScrollBar2: TScrollBar;
    Button2: TButton;
    lblLifeOrientation: TLabel;
    lblResults: TLabel;
    lblPureMaths: TLabel;
    lblPhysics: TLabel;
    lblLifeScience: TLabel;
    sedIT: TSpinEdit;
    btnSigningUp: TButton;
    btnCalcAvgScore: TButton;
    sedLifeSci: TSpinEdit;
    redAPS: TRichEdit;
    sedPhy: TSpinEdit;
    sedMath: TSpinEdit;
    sedLO: TSpinEdit;
    tbsSignUp: TTabSheet;
    btnCreateOwn: TButton;
    edtStudIDI: TEdit;
    edtNameI: TEdit;
    edtSNameI: TEdit;
    btnLogin: TButton;
    btnGenerate: TButton;
    btnBack: TButton;
    lblLanguage: TLabel;
    lblQuestion: TLabel;
    lblOption: TLabel;
    lblStudID: TLabel;
    Label4: TLabel;
    Label3: TLabel;
    lblSignUp: TLabel;
    tbsLogin: TTabSheet;
    btnDone: TButton;
    Label5: TLabel;
    lblFindAcc: TLabel;
    lblForgotPass: TLabel;
    lblPassword: TLabel;
    lblStudentId: TLabel;
    edtPass: TEdit;
    edtUserID: TEdit;
    btnSettings: TButton;
    btnBackk: TButton;
    tbsAccount: TTabSheet;
    tbsZoom: TTabSheet;
    Image2: TImage;
    Label6: TLabel;
    Button3: TButton;
    Button4: TButton;
    Button5: TButton;
    btnMeeting: TButton;
    edtDayTime: TEdit;
    sgdTimeTable: TStringGrid;
    btnShowTimeTable: TButton;
    lblTimeDay: TLabel;
    btnBackkk: TButton;
    btnSettingss: TButton;
    procedure ScrollBar2Change(Sender: TObject);
    Function studentidGenerate: string;
    procedure btnWriteClick(Sender: TObject);
    procedure FormCreate(Sender: TObject);
    procedure btnSubmitClick(Sender: TObject);
    Function getGender: string;
    procedure btnGenerateClick(Sender: TObject);
  private
    { Private declarations }
    objNML: TNML;
  public
    { Public declarations }
  end;

var
  frmOnlineEdu: TfrmOnlineEdu;
  sSurname, sName, sId, sCell, sHomeL, sHomeNo, sAddress, sPostal, sSchool,
    sDate, sYear, sCourseOptI, sCourseOptII, sCourseOptIII: string;
  sStudentIde: string;

implementation

{$R *.dfm}

procedure TfrmOnlineEdu.btnGenerateClick(Sender: TObject);
var
  sSurnameI, sNameI, sStudentIDI, sPasswordI: string;
  sSQL: string;
begin
  sSurnameI := edtSNameI.Text;
  sNameI := edtNameI.Text;
  sStudentIDI := edtStudIDI.Text;

  sPasswordI := Copy(sSurnameI, 2, 2) + Copy(sStudentIDI, 3, 2) +
    Copy(sNameI, 3, 2) + Copy(sStudentIDI, 6, 2);

  with dmTables do
  begin
    adqAccount.Active := true;
    adqAccount.SQL.Clear;
    sSQL := 'Insert Into tblAccounts(StudentID,stSurname,stName,stPassword) Values('''
      + sStudentIDI + ''',''' + sSurnameI + ''',''' + sNameI + ''',''' +
      sPasswordI + ''' ) ';
    adqAccount.SQL.Add(sSQL);
    adqAccount.Open;
  end;
 // showMessage(''A)
 //showmesssa
end;

procedure TfrmOnlineEdu.btnSubmitClick(Sender: TObject);
begin // TADOTable
  with dmTables do
  begin
    tblUserDetails.Append;
    tblUserDetails['uID'] := sId;
    tblUserDetails['uSurname'] := sSurname;
    tblUserDetails['uName'] := sName;
    tblUserDetails['uCellNo'] := sCell;
    tblUserDetails['uHomeNo'] := sHomeNo;
    tblUserDetails['uHomeLang'] := sHomeL;
    tblUserDetails['uAddress'] := sAddress;
    tblUserDetails['uPostal'] := sPostal;
    tblUserDetails['uGender'] := getGender;
    tblUserDetails.Post;

    tblStudent.Append;
    tblStudent['studentID'] := studentidGenerate;
    tblStudent['uID'] := sId;
    tblStudent['uApplyDate'] := sDate;
    tblStudent['uYear'] := sYear;
    tblStudent['uCourseOpt1'] := sCourseOptI;
    tblStudent['uCourseOpt2'] := sCourseOptII;
    tblStudent['uCourseOpt3'] := sCourseOptIII;
    tblStudent.Post;
  end;
end;

procedure TfrmOnlineEdu.btnWriteClick(Sender: TObject);
begin
  // ShowMessage(studentidGenerate);
  frmMasterAcc.Show;
  frmOnlineEdu.Hide;
end;

procedure TfrmOnlineEdu.FormCreate(Sender: TObject);
begin
  sSurname := edtSurname.Text;
  sName := edtName.Text;
  sId := edtID.Text;
  sCell := edtCellNo.Text;
  sHomeL := edtHL.Text;
  sHomeNo := edtHomeNo.Text;
  sAddress := edtHomeAddress.Text;
  sPostal := edtPostal.Text;
  sSchool := edtHighSchool.Text;
  sDate := edtApplyDate.Text;
  sYear := cbxYear.Items[cbxYear.ItemIndex];
  sCourseOptI := cbxOptI.Items[cbxOptI.ItemIndex];
  sCourseOptII := cbxOptII.Items[cbxOptII.ItemIndex];
  sCourseOptIII := cbxOptIII.Items[cbxOptIII.ItemIndex];
end;

function TfrmOnlineEdu.getGender: string;
begin // RadioGroup1.Items[RadioGroup1.ItemIndex];
  if (rgpGender.Items[rgpGender.ItemIndex] = 'female') then
  begin
    Result := 'female';
  end
  else if (rgpGender.Items[rgpGender.ItemIndex] = 'male') then
  begin
    Result := 'male';
  end;
end;

function TfrmOnlineEdu.studentidGenerate: string;
begin
  Result := sName[1] + sSurname[1] + Copy(sDate, 9, 2) + Copy(sDate, 6, 2) +
    Copy(cbxYear.Text, 4, 1) + '1' + 'k';
end;

procedure TfrmOnlineEdu.ScrollBar2Change(Sender: TObject);
begin
  // TabSheet4.Top:=TScrollBar.P
end;

end.
